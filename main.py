from ultralytics import YOLO



# # Load a model
model = YOLO("yolov8n.yaml")
model = YOLO("yolov8n.pt")
model = YOLO("yolov8n.yaml").load("yolov8n.pt")

# Use the model
results = model.train(data="C:\\Users\\parth\\D3 Fire Detector\\code\\Smoke and fire\\config.yaml", epochs=25)  # train the model
