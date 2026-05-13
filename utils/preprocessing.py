def normalize_landmarks(landmarks):
    base_x, base_y = landmarks[0]

    normalized = []

    for x, y in landmarks:
        normalized.append(x - base_x)
        normalized.append(y - base_y)

    return normalized