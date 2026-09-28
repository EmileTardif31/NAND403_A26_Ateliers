from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTextEdit, QPushButton, QMessageBox
 
class MessageBoard(QWidget):
    def __init__(self): # Constructeur
        super().__init__() # Constructeur QWidget
        self.setWindowTitle("Message board")
        self.create_ui()
 
    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Message board")
        layout.addWidget(label)
 
        # QTextEdit
        text_box = QTextEdit(self)
        # text_box.placeholderText() = "du texte"
        layout.addWidget(text_box)
 
        # QPushButton
        button = QPushButton(self)
        button.setText("bouton")
        layout.addWidget(button)
        button.clicked.connect(self.on_click)
   
    def on_click(self):
        print("on click called")
        # QMessageBox
   
 
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()