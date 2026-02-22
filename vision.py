import cv2
from ultralytics import YOLO
import socket

# 1. Setup Network Connection (to talk to C++)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("127.0.0.1", 5005)

# 2. Load the AI Model
model = YOLO('yolov8n.pt') 
cap = cv2.VideoCapture("traffic.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    # Run Detection
    results = model(frame)
    car_count = 0
    
    for box in results[0].boxes:
        if int(box.cls) in [2, 3, 5, 7]: # COCO classes for car, motorcycle, bus, truck
            car_count += 1

    # 3. Send count to the C++ "Controller"
    message = str(car_count).encode()
    client_socket.sendto(message, addr)

    # Show the video
    cv2.imshow("Smart Camera Feed", results[0].plot())
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()