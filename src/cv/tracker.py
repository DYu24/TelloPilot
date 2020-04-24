import sys
import cv2

sys.path.append('..')

from cv.face_detector import FaceDetector

class Tracker:
    def __init__(self, drone):
        self.drone = drone
        self.face_detector = FaceDetector()

    def track_face(self, image, speed):
        img, faces = self.face_detector.detect_face(image)

        self._mark_image_center(img)

        if (len(faces) > 0):
            self._mark_face_center(img, faces[0])
            fx, fy, fw, fh = faces[0]
            delta_x = (int(fw / 2) + fx) - (img.shape[1] / 2)
            delta_y = (int(fh / 2) + fy) - (img.shape[0] / 2)

            # Track horizontal plane
            if abs(delta_x) > fw / 2:
                if delta_x > 0:
                    print('Move camera right')
                    self.drone.clockwise(speed)
                else:
                    print('Move camera left')
                    self.drone.counter_clockwise(speed)
            elif abs(delta_x) < fw / 2:
                if delta_x > 0:
                    self.drone.clockwise(0)
                else:
                    self.drone.counter_clockwise(0)

            # Track vertical plane
            if abs(delta_y) > fh / 2:
                if delta_y > 0:
                    print('Move camera down')
                    self.drone.down(speed)
                else:
                    print('Move camera up')
                    self.drone.up(speed)
            elif abs(delta_x) < fw / 2:
                if delta_y > 0:
                    self.drone.down(0)
                else:
                    self.drone.up(0)
        # Don't move if there are no faces
        else:
            self.drone.clockwise(0)
            self.drone.counter_clockwise(0)

        return img

    def _mark_image_center(self, image):
        x = int(image.shape[1] / 2)
        y = int(image.shape[0] / 2)
        cv2.rectangle(image, (x, y), (x + 5, y + 5), (255, 0, 0), 2)

    def _mark_face_center(self, image, face):
        x, y, w, h = face
        mid_x = int(w / 2)
        mid_y = int(h / 2)
        roi = image[y:y+h, x:x+w]
        cv2.rectangle(roi, (mid_x, mid_y), (mid_x + 5, mid_y + 5), (0, 0, 255), 2)


if __name__ == '__main__':
    fd = FaceDetector()
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        ret, img = cap.read()

        img, faces = fd.detect_face(img)
        height, width, channels = img.shape

        x = int(width / 2)
        y = int(height / 2)
        cv2.rectangle(img, (x, y), (x + 5, y + 5), (255, 0, 0), 2)

        if (len(faces) > 0):
            fx, fy, fw, fh = faces[0]
            delta_x = (int(fw / 2) + fx) - x
            delta_y = (int(fh / 2) + fy) - y

            if abs(delta_x) > fw / 2:
                if delta_x > 0:
                    print('Move camera right')
                else:
                    print('Move camera left')

            if abs(delta_y) > fh / 2:
                if delta_y > 0:
                    print('Move camera down')
                else:
                    print('Move camera up')

        cv2.imshow('Face', img)
        cv2.waitKey(1)