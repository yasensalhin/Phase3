import cv2
from threading import Thread
from time import sleep

class Camera:
    def __init__(self) -> None:
        self._cap = cv2.VideoCapture()
        self._cap.open(0)

        self._frame = None

        self._frame_thread = Thread(target=self._frame_loop, daemon=True)
        self._frame_thread.start()

    def _frame_loop(self):
        while True:
            success, image = self._cap.read()
            if success:
                self._frame = image
            else:
                print("Failed to read from camera, retrying...")
                self._cap.release()
                self._cap.open(0) 
            sleep(0.015)  

    @property
    def frame(self):
        return self._frame
