import cv2

class FaceDetector:
    def __init__(self):
        # Paths are taken relative from where the main script is run
        self.face_cascade = cv2.CascadeClassifier('./cv/cascades/haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier('./cv/cascades/haarcascade_eye_tree_eyeglasses.xml')

    def detect_face(self, image):
        color_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # scaleFactor = 1.3, minNeighbors = 5
        faces = self.face_cascade.detectMultiScale(gray_image, 1.3, 5)

        for x, y, w, h in faces:
            cv2.rectangle(color_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray_image[y:y+h, x:x+w]
            roi_color = color_image[y:y+h, x:x+w]

            eyes = self.eye_cascade.detectMultiScale(roi_gray)
            for ex, ey, ew, eh in eyes:
                cv2.rectangle(roi_color, (ex,ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        return color_image
