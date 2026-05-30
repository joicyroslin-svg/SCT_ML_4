# ==================================================
# SCT_ML_4 - Hand Gesture Recognition
# Corrected Version
# ==================================================

import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75
)


def get_finger_states(hand_landmarks, hand_label):
    """
    Returns finger states:
    1 = finger is open
    0 = finger is closed
    Order: [thumb, index, middle, ring, pinky]
    """

    finger_states = []

    # Landmark IDs
    thumb_tip = 4
    thumb_ip = 3

    finger_tips = [8, 12, 16, 20]
    finger_pips = [6, 10, 14, 18]

    # -------------------------------
    # Thumb detection based on hand side
    # -------------------------------
    if hand_label == "Right":
        if hand_landmarks.landmark[thumb_tip].x < hand_landmarks.landmark[thumb_ip].x:
            finger_states.append(1)
        else:
            finger_states.append(0)
    else:
        if hand_landmarks.landmark[thumb_tip].x > hand_landmarks.landmark[thumb_ip].x:
            finger_states.append(1)
        else:
            finger_states.append(0)

    # -------------------------------
    # Other fingers detection
    # -------------------------------
    for tip, pip in zip(finger_tips, finger_pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            finger_states.append(1)
        else:
            finger_states.append(0)

    return finger_states


def is_thumbs_up(hand_landmarks):
    """
    Special rule for Thumbs Up gesture.
    This works better than normal thumb detection.
    """

    thumb_tip = hand_landmarks.landmark[4]
    thumb_ip = hand_landmarks.landmark[3]
    thumb_mcp = hand_landmarks.landmark[2]

    index_tip = hand_landmarks.landmark[8]
    index_pip = hand_landmarks.landmark[6]

    middle_tip = hand_landmarks.landmark[12]
    middle_pip = hand_landmarks.landmark[10]

    ring_tip = hand_landmarks.landmark[16]
    ring_pip = hand_landmarks.landmark[14]

    pinky_tip = hand_landmarks.landmark[20]
    pinky_pip = hand_landmarks.landmark[18]

    thumb_is_up = thumb_tip.y < thumb_ip.y < thumb_mcp.y

    fingers_are_closed = (
        index_tip.y > index_pip.y and
        middle_tip.y > middle_pip.y and
        ring_tip.y > ring_pip.y and
        pinky_tip.y > pinky_pip.y
    )

    return thumb_is_up and fingers_are_closed


def classify_gesture(fingers, hand_landmarks):
    """
    Classifies hand gesture based on finger states.
    """

    thumb, index, middle, ring, pinky = fingers

    # Special check first
    if is_thumbs_up(hand_landmarks):
        return "Thumbs Up"

    if fingers == [0, 0, 0, 0, 0]:
        return "Fist"

    elif fingers == [1, 1, 1, 1, 1]:
        return "Open Palm"

    elif index == 1 and middle == 0 and ring == 0 and pinky == 0:
        return "Pointing"

    elif index == 1 and middle == 1 and ring == 0 and pinky == 0:
        return "Victory"

    elif thumb == 1 and index == 1 and middle == 0 and ring == 0 and pinky == 0:
        return "L Shape"

    elif pinky == 1 and index == 0 and middle == 0 and ring == 0:
        return "Pinky"

    else:
        return "Unknown Gesture"


# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam not opening.")
    exit()

print("Hand Gesture Recognition Started")
print("Press 'q' to quit")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Frame not captured.")
        break

    # Flip frame for natural selfie view
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame
    result = hands.process(rgb_frame)

    gesture = "No Hand Detected"
    hand_label = "Unknown"
    fingers = []

    if result.multi_hand_landmarks and result.multi_handedness:
        for hand_landmarks, handedness in zip(
            result.multi_hand_landmarks,
            result.multi_handedness
        ):

            # Get left/right hand label
            hand_label = handedness.classification[0].label

            # Draw landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Get finger states
            fingers = get_finger_states(hand_landmarks, hand_label)

            # Classify gesture
            gesture = classify_gesture(fingers, hand_landmarks)

    # Display output
    cv2.putText(
        frame,
        f"Hand: {hand_label}",
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Fingers: {fingers}",
        (10, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Gesture: {gesture}",
        (10, 115),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        3
    )

    cv2.imshow("SCT_ML_4 - Hand Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()