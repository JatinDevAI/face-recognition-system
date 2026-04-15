import cv2
import face_recognition
import os

# -------------------------------
# SETTINGS
# -------------------------------
KNOWN_FACES_DIR = "known_faces"
TOLERANCE = 0.5  # lower = stricter recognition

# -------------------------------
# CHECK FOLDER
# -------------------------------
if not os.path.exists(KNOWN_FACES_DIR):
    print("❌ Folder 'known_faces' not found. Please create it.")
    exit()

# -------------------------------
# LOAD KNOWN FACES
# -------------------------------
known_encodings = []
known_names = []

for file in os.listdir(KNOWN_FACES_DIR):
    try:
        img_path = os.path.join(KNOWN_FACES_DIR, file)
        img = face_recognition.load_image_file(img_path)

        encodings = face_recognition.face_encodings(img)

        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            known_names.append(os.path.splitext(file)[0])
        else:
            print(f"⚠️ No face found in {file}, skipped.")

    except Exception as e:
        print(f"Error loading {file}: {e}")

print("✅ Faces Loaded:", known_names)

# -------------------------------
# AUTO CAMERA DETECTION (Fix OBS issue)
# -------------------------------
def get_working_camera():
    for i in range(5):
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        if cap.isOpened():
            print(f"✅ Using Camera Index: {i}")
            return cap
    return None

cap = get_working_camera()

if cap is None:
    print("❌ No camera found!")
    exit()

# -------------------------------
# MAIN LOOP
# -------------------------------
while True:
    ret, frame = cap.read()

    if not ret:
        print("⚠️ Failed to grab frame")
        break

    # Resize for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_small)
    face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        # Scale back up
        top *= 2
        right *= 2
        bottom *= 2
        left *= 2

        name = "Unknown"

        if len(known_encodings) > 0:
            distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = distances.argmin()

            if distances[best_match_index] < TOLERANCE:
                name = known_names[best_match_index]

        # Draw rectangle
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Label
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Face Recognition AI", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -------------------------------
# CLEANUP
# -------------------------------
cap.release()
cv2.destroyAllWindows()