from ultralytics import YOLO


# Load a model
model = YOLO('yolov8n.yaml')  # build a new model from YAML

# Train the model
results = model.train(data='/content/CSE493-Final/CSE493-Final/detection/ee443.yaml', epochs=100, imgsz=640)
