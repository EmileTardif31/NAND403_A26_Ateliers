from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTextEdit, QPushButton, QMessageBox
 
class MessageBoard(QWidget):
    def __init__(self): # Constructeur
        super().__init__() # Constructeur QWidget
        self.setWindowTitle("Warning Generator")
        self.create_ui()
 
    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Warning Message")
        layout.addWidget(label)
 
        global text_box
        text_box = QTextEdit(self)
        # text_box.placeholderText() = "du texte"
        layout.addWidget(text_box)
 
        button = QPushButton(self)
        button.setText("Générer un warning")
        layout.addWidget(button)
        button.clicked.connect(self.on_click)
   
    def on_click(self):
        messageBox = QMessageBox.warning(
            self,
            "Mon texte",
            text_box.toPlainText()
        )
   
 
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()