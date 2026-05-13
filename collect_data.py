import cv2
import csv
from utils.hand_detector import HandDetector
from utils.preprocessing import normalize_landmarks

cap = cv2.VideoCapture(0)
detector = HandDetector()

label = input("Enter Sign Label (A/B/C/D/E): ")

max_samples = 300
count = 0

with open("data/sign_data.csv", mode="a", newline="") as file:
    writer = csv.writer(file)

    while True:
        success, img = cap.read()
        if not success:
            print("Camera not working")
            break

        img = cv2.flip(img, 1)

        img, landmarks = detector.detect_hand(img)

        if len(landmarks) == 21:
            data = normalize_landmarks(landmarks)
            data.append(label)

            writer.writerow(data)

            count += 1
            print(f"Saved: {count}/{max_samples}")

        cv2.putText(
            img,
            f"{label}: {count}/{max_samples}",
            (10, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("Collect Data", img)

        if count >= max_samples:
            print("Collection Done!")
            break

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()