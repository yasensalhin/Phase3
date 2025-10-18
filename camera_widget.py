import cv2
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSizePolicy, QApplication
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap
import numpy as np
class CameraWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.is_camera_on = False
        self.cap = None

       
        self.label = QLabel("Camera Feed")
        self.label.setStyleSheet("background-color: black; color: white; font-size: 32px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        
        self.start_btn = QPushButton("Start Camera")
        self.info_label = QLabel("Status: OFF")
        self.info_label.setAlignment(Qt.AlignCenter)

        
        self.start_btn.clicked.connect(self.toggle_camera)
    

        controls_layout = QVBoxLayout()
        controls_layout.addWidget(self.start_btn)
        controls_layout.addStretch()
        controls_layout.addWidget(self.info_label)

        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label, stretch=3)
        main_layout.addLayout(controls_layout, stretch=1)

        self.setLayout(main_layout)

        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

    def toggle_camera(self):
        if not self.is_camera_on:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                self.label.setText("❌ Failed to open camera")
                self.info_label.setText("Status: ERROR")
                return

            self.is_camera_on = True
            self.start_btn.setText("Stop Camera")
            self.info_label.setText("Status: ON")
            self.timer.start(30)
        else:
            self.is_camera_on = False
            self.timer.stop()
            if self.cap:
                self.cap.release()
                self.cap = None
            self.start_btn.setText("Start Camera")
            self.label.setText("Camera Stopped")
            self.info_label.setText("Status: OFF")

    

    def update_frame(self):
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = frame.shape
                bytes_per_line = ch * w
                image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(image)

            
                label_w = self.label.width()
                label_h = self.label.height()

            
                pixmap = QPixmap.fromImage(image)
                self.label.setPixmap(
                    pixmap.scaled(
                        self.label.width(),
                        self.label.height(),
                        Qt.IgnoreAspectRatio,         
                        Qt.SmoothTransformation        
                )
                )

    def rescaleFrame(size,frame,scale=0.75):
        width=(int)(frame.shape[1]*scale)
        height=(int)(frame.shape[0]*scale)
        dimensions=(width,height)
        return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

    
if __name__ == "__main__":
    app = QApplication([])
    w = CameraWidget()
    w.show()
    app.exec()

    app.exec()

