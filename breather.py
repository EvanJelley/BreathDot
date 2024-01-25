from PySide6.QtWidgets import QApplication, QMainWindow, QRadioButton, QLabel, QVBoxLayout,QWidget

# Only needed for access to command line arguments
import sys

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("The Breather")

        # Set in Breath Radio options
        inLabel = QLabel("How long would you like your intake to be?")
        in3 = QRadioButton("3 seconds")
        in4 = QRadioButton("4 seconds")
        in5 = QRadioButton("5 seconds")
        in6 = QRadioButton("6 seconds")
        in3.setCheckable(True)
        in4.setCheckable(True)
        in5.setCheckable(True)
        in6.setCheckable(True)
        in3.clicked.connect(self.startOnClick)

        # Create a QVBoxLayout instance
        layout = QVBoxLayout()

        # Add your widgets to the layout
        layout.addWidget(inLabel)
        layout.addWidget(in3)
        layout.addWidget(in4)
        layout.addWidget(in5)
        layout.addWidget(in6)

        # Create a QWidget and set it as the central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def startOnClick(self):
        print("Start button clicked")



app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()

# Start the event loop.
app.exec()

# Your application won't reach here until you exit and the event
# loop has stopped.