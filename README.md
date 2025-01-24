# AssistX YOLOv8 Inference Dockerized Solution

## Steps Overview

1. **Model Selection**:
   The YOLOv8 model (`yolov8n.pt`) was chosen for object detection tasks because it supports both CPU and GPU environments.

2. **Inference Script**:
   The `run_inference.py` script handles the detection task by using the YOLOv8 model. It accepts an image or video file as input and saves the output in a specified directory.

3. **Dockerizing the Application**:
   The solution is packaged in a Docker container, with a Dockerfile specifying Python dependencies and additional system libraries. The image is built using `python:3.9-buster` as the base.

4. **Docker Commands for CPU/GPU**:
   - To run the model on CPU:
     ```bash
     docker run --rm -v <local_directory>:/app abcdullahh/assistx-yolov5 python /app/run_inference.py /app/input/<image_or_video>
     ```
   - To run the model on GPU (with `--gpus all` flag):
     ```bash
     docker run --rm --gpus all -v <local_directory>:/app abcdullahh/assistx-yolov5 python /app/run_inference.py /app/input/<image_or_video>
     ```

5. **Testing**:
   The solution has been tested both locally and after dockerizing. Tests were conducted with both CPU and GPU setups to ensure the model functions correctly.

## How to Run

1. **Clone this repository**:
   ```bash
   git clone https://github.com/ABCDullahh/ML_Model_AssistX.git
   ```

2. **Build Docker Image**:
   ```bash
   docker build -t abcdullahh/assistx-yolov5 .
   ```

3. **Run the Docker Container**:
   - For CPU:
     ```bash
     docker run --rm -v <local_directory>:/app abcdullahh/assistx-yolov5 python /app/run_inference.py /app/input/<image_or_video>
     ```
   - For GPU:
     ```bash
     docker run --rm --gpus all -v <local_directory>:/app abcdullahh/assistx-yolov5 python /app/run_inference.py /app/input/<image_or_video>
     ```

4. **Push Docker Image to DockerHub**:
   ```bash
   docker push abcdullahh/assistx-yolov5:latest
   ```

## Links
- **GitHub Repository**: [https://github.com/ABCDullahh/ML_Model_AssistX](https://github.com/ABCDullahh/ML_Model_AssistX)
- **Google Drive for Test Images/Videos**: [Google Drive Folder](https://drive.google.com/drive/folders/1I7q8R8PUX4KsaFdXx6zZFOvz8PpUJfXe?usp=sharing)
-  **Google Drive for the Solutions Document** : [Google Drive](https://drive.google.com/file/d/1Uvk54ZGGLSivtyemjz8ZHDQ4yIdJpL3X/view?usp=sharing)
