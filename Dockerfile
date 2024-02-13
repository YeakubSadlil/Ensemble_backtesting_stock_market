# Base Image
FROM python:3.10

# Project Setup
WORKDIR /app 
COPY requirements.txt ./

# Install dependencies for TA-lib
RUN apt-get update && apt-get install -y \
    build-essential python3-dev 

# TA-Lib Installation from Source, it is required for zipline
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
    tar -xzf ta-lib-0.4.0-src.tar.gz && \
    cd ta-lib/ && \
    ./configure && \
    make && \
    make install
    
RUN pip install -r requirements.txt

# Copy Project Files
COPY . .  

# Specify Entry Point
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
