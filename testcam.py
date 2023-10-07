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
model = YOLO('C:\\Users\\parth\\D3 Fire Detector\\code\\data\\MainCode\\runs\\detect\\train4\\weights\\best.pt')  # best.pt
# model = YOLO('C:\\Users\\parth\\D3 Fire Detector\\code\\data\\MainCode\\runs\\detect\\train3\\weights\\last.pt')  # last.pt


capture_images()

# results= model.predict("C:\\Users\\parth\\D3 Fire Detector\\code\\data\\images\\test\\download.jpg")
# results= model.predict("C:\\Users\\parth\\D3 Fire Detector\\code\\data\\images\\test\\photo-1612251485013-58be9e5689c3.jpg")
# cv2.imshow()
