FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for soundfile
RUN apt-get update && apt-get install -y \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# -----------PYTHON PACKAGES---------------------
RUN pip install --no-cache-dir \
    numpy \
    soundfile \
    optimum-intel \
    transformers \
    torch \
    openvino

#----------------------------DEVELOPMENT PACKAGES--------------
RUN pip install --no-cache-dir \
    uvicorn \
    fastapi


