FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for soundfile
RUN apt-get update && apt-get install -y \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# -----------PYTHON PACKAGES---------------------
# Install PyTorch CPU-only version first
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install other packages ensuring CPU-only versions where applicable
RUN pip install --no-cache-dir \
    numpy \
    soundfile \
    "optimum-intel[openvino]" \
    transformers \
    --extra-index-url https://download.intel.com/ipex/cpu-runtime-pip-wheels

# Install Piper TTS
RUN pip install --no-cache-dir piper-tts

# Development packages
RUN pip install --no-cache-dir \
    uvicorn \
    fastapi

RUN pip install openai==0.28