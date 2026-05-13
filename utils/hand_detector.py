import cv2
import mediapipe as mp


class HandDetector:
    def __init__(self, max_hands=1):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=max_hands)
        self.mp_draw = mp.solutions.drawing_utils

    def detect_hand(self, img):
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb_img)

        landmark_list = []

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                for lm in hand_landmarks.landmark:
                    landmark_list.append([lm.x, lm.y])

                self.mp_draw.draw_landmarks(
                    img,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

        return img, landmark_list