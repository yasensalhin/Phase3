from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import (
    QWidget, QMainWindow, QVBoxLayout, QLabel, QHBoxLayout, QToolBar,QSizePolicy
)
from PySide6.QtCore import Qt
from camera_widget import CameraWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(640, 480)
        self.setWindowTitle("Robot Control Panel")

        
        self.camera = CameraWidget()
        self.camera.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)

        self.v_layout = QVBoxLayout()
        container = QWidget()
        container.setLayout(self.v_layout)
        self.setCentralWidget(container)


        self.h_layout = QHBoxLayout()
        self.coords_display = QLabel(self.x_y_values(2, 3))
        self.connected_to_mqtt = QLabel(self.MQTT_connection(True))

        self.coords_display.setAlignment(Qt.AlignLeft)
        self.connected_to_mqtt.setAlignment(Qt.AlignRight)

        self.h_layout.addWidget(self.coords_display)
     
        self.h_layout.addWidget(self.connected_to_mqtt)
        
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.camera)



        self.show()

    def x_y_values(self, x, y) -> str:
        return f"X:{x} , Y:{y}"

    def MQTT_connection(self, status_of_Mqtt: bool) -> str:
        if status_of_Mqtt:
            return "<span style='color:green;'>✅ Connected To The Robot</span>"
        return "<span style='color:red;'>❌ Robot Not Connected</span>"
