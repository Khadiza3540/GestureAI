import cv2
from utils.hand_detector import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector()

while True:
    success, img = cap.read()

    if not success:
        print("Camera not working")
        break

    img = cv2.flip(img, 1)
    img, landmarks = detector.detect_hand(img)

    if len(landmarks) != 0:
        print(len(landmarks))

    cv2.imshow("GestureAI", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()