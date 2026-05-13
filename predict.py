import cv2
import pickle
from utils.hand_detector import HandDetector
from utils.preprocessing import normalize_landmarks

# Load trained model
with open("models/sign_model.pkl", "rb") as f:
    model = pickle.load(f)

# Start camera
cap = cv2.VideoCapture(0)
detector = HandDetector()

# Smooth prediction variables
prev_prediction = ""
count = 0
stable_prediction = ""

while True:
    success, img = cap.read()
    if not success:
        print("Camera not working")
        break

    img = cv2.flip(img, 1)

    # Detect hand
    img, landmarks = detector.detect_hand(img)

    if len(landmarks) == 21:
        # Normalize landmarks
        data = normalize_landmarks(landmarks)

        # Predict sign
        prediction = model.predict([data])[0]

        # Smooth prediction logic
        if prediction == prev_prediction:
            count += 1
        else:
            count = 0
            prev_prediction = prediction

        if count > 5:
            stable_prediction = prediction

        # Show stable sign
        if stable_prediction != "":
            cv2.putText(
                img,
                f"Sign: {stable_prediction}",
                (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                2,
                (0, 255, 0),
                3
            )

    cv2.imshow("Sign Language Prediction", img)

    # ESC press korle close
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()