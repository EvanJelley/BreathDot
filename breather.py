from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QRadioButton,
    QLabel,
    QVBoxLayout,
    QWidget,
    QButtonGroup,
)
from PySide6.QtGui import QPixmap, QPainter, QColor
from PySide6.QtCore import QPropertyAnimation, QRect, QSequentialAnimationGroup, QPoint

# Only needed for access to command line arguments
import sys

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #### LAYOUT INITIALIZATION ####
        # Set some main window's properties
        self.setWindowTitle("The Breather")        

        # Create a QVBoxLayout instance
        layout = QVBoxLayout()

        # Create a QWidget, set its layout to the QVBoxLayout, and set it as the central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        #### RADIO BUTTON MENU INITIALIZATION ####
        # Set in Breath Radio options
        inLabel = QLabel("How long would you like your intake to be?")
        inRadioButtons = []
        for i in range(3, 7):
            inButton = QRadioButton(f"{i} seconds")
            inRadioButtons.append(inButton)
        
        #Create a button group for intake options
        self.inGroup = QButtonGroup(self)
        for button in inRadioButtons:
            self.inGroup.addButton(button)

        # Set out Breath Radio options
        outLabel = QLabel("How long would you like your outtake to be?")
        outRadioButtons = []
        for i in range(3, 7):
            outButton = QRadioButton(f"{i} seconds")
            outRadioButtons.append(outButton)
        
        #Create a button group for outtake options
        self.outGroup = QButtonGroup(self)
        for button in outRadioButtons:
            self.outGroup.addButton(button)

        # Add your widgets to the layout
        layout.addWidget(inLabel)
        for button in inRadioButtons:
            layout.addWidget(button)
        layout.addWidget(outLabel)
        for button in outRadioButtons:
            layout.addWidget(button)

        # Connect selections to methods
        for button in inRadioButtons:
            button.clicked.connect(self.inBreathTime)
        for button in outRadioButtons:
            button.clicked.connect(self.outBreathTime)
        
        #### DOT CREATION AND ANIMATION ####
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red;border-radius:10px;")
        self.child.resize(20, 20)
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setEndValue(QPoint(400, 400))
        self.anim.setDuration(1500)
        self.anim.start()

    # Create methods to set the breath times
    def inBreathTime(self):
        for button in self.inGroup.buttons():
            if button.isChecked():
                self.inBreathTime = int(button.text()[0])
                print(f"Breath in time: {self.inBreathTime}")

    def outBreathTime(self):
        for button in self.outGroup.buttons():
            if button.isChecked():
                self.outBreathTime = int(button.text()[0])
                print(f"Breath out time: {self.outBreathTime}")
    



app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()

# Start the event loop.
app.exec()

# Your application won't reach here until you exit and the event
# loop has stopped.