#Live webcam feed check : BACKEND CAMERA TEST AND PREDICT PROTOTYPE


from ultralytics import YOLO
import cv2

def capture_images():
      vid = cv2.VideoCapture(0)

      while True:
            ret, frame = vid.read()

            pred= model.predict(frame)


            if ret==True:
                  results=model(source=frame, show=True, conf=0.6)

            if cv2.waitKey(1) & 0xFF == ord('0'):
                  break
    
      vid.release()
      cv2.destroyAllWindows()


model = YOLO("yolov8n.pt")
model = YOLO('best.pt')  # best.pt
# model = YOLO('last.pt')  # last.pt


capture_images()

