from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout,QSizePolicy
from PySide6.QtCore import Qt

from RobotGui.gui.camera_display import CameraDisplay
from RobotGui.gui.coordinates_display import Coordinates_display
from RobotGui.core.comm.client import MQTTClient


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(640, 480)
        
        self.setCentralWidget(CentralWidget())
        self.show()
        self._myMqttclient=MQTTClient()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        changed = False
        self._movement= None

        if event.key()==Qt.Key.Key_Up:
            self._movement="Up"
            changed = True
        elif event.key()==Qt.Key.Key_Down:
            self._movement="Down"
            changed=True
        elif event.key()==Qt.Key.Key_Right:
            self._movement="Right"
            changed=True
        elif event.key()==Qt.Key.Key_Left:
            self._movement="Left"
            changed=True
        else:
            pass

        if changed:
            self._myMqttclient.publish_motion(self._movement)
        else :
            pass
            

class CentralWidget(QWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self._layout = QVBoxLayout(self)

        self._camera_widget = CameraDisplay()
        self._layout.addWidget(self._camera_widget)
        

        self._coordinates_widget = Coordinates_display()
        self._coordinates_widget.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)

        self._myMqttclient=MQTTClient()
        self._myMqttclient.setup(self._coordinates_widget.update_coordinates)
        self._layout.addWidget(self._coordinates_widget)
