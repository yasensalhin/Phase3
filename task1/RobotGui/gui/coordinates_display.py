from PySide6.QtWidgets import QWidget,QLabel,QSizePolicy,QVBoxLayout
from PySide6.QtCore import Slot,Qt

class Coordinates_display(QWidget):
    def __init__(self,parent:QWidget |None=None):
        super().__init__(parent)

        self._label=QLabel(self)
        self._label.setText('Robot is not connected.')
        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._label.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        self._label.setWordWrap(True)
        layout = QVBoxLayout(self)
        layout.addWidget(self._label)

    @Slot()
    def update_coordinates(self,x:float,y:float):
        self._label.setText(f'Robot is present at: {x}, {y}')


        
        
     