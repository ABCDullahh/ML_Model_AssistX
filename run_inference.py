import torch
from ultralytics import YOLO
import sys

def run_inference(input_path: str, output_dir: str = "results"):
    # cek(GPU atau CPU)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Model is running on {device}") 
    
    # inisialisasi model YOLOv8
    model = YOLO("yolov8n.pt").to(device)

    # predict input file dengan model
    results = model.predict(source=input_path, project=output_dir, name="detect", save=True)

    # output
    output_files = [r.path for r in results]
    if len(output_files) > 0:
        return output_files[0]
    else:
        return ""

if __name__ == "__main__":
    # command line local: python run_inference.py <path_input> <output_dir?>
    if len(sys.argv) < 2:
        print("Usage: python run_inference.py <input_image_or_video> [<output_dir>]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "results"

    output_path = run_inference(input_path, output_dir)
    print(f"Hasil disimpan di: {output_path}")