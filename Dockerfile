# base image
FROM python:3.9-buster

# working directory
WORKDIR /app

# dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt instal dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy semua file ke dalam container
COPY . .

# run script
CMD ["python", "run_inference.py"]