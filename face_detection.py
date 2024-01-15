import cv2

video_cap = cv2.VideoCapture(0) 
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

while True:
    if cv2.waitKey(10) == ord("a"):
        break
    ret, video_data = video_cap.read()
    face = face_classifier.detectMultiScale(
    video_data, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)
    for (x, y, w, h) in face:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 4)
    cv2.imshow("Live", video_data)
    
print("HI")
video_cap.release()