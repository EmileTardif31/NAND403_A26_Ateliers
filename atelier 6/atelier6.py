import maya.cmds as cmds

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTextEdit, QPushButton, QSpinBox
 
class MessageBoard(QWidget):
    def __init__(self): # Constructeur
        super().__init__() # Constructeur QWidget
        self.setWindowTitle("Fence generator")
        self.setFixedWidth(250)
        self.create_ui()
 
    def create_ui(self):

        layout = QVBoxLayout(self)

        # -- longueur poteau haut
        label = QLabel("Pillar Height")
        layout.addWidget(label)

        global haut_longueur
        haut_longueur = QSpinBox(self)
        haut_longueur.setRange(4, 10) # set la range
        haut_longueur.setValue(6) # valeur par défaut
        layout.addWidget(haut_longueur)

        # -- largeur poteau haut
        label = QLabel("Pillar Width (/10)")
        layout.addWidget(label)

        global haut_largeur
        haut_largeur = QSpinBox(self)
        haut_largeur.setRange(1, 10) # set la range
        haut_largeur.setValue(9) # valeur par défaut
        layout.addWidget(haut_largeur)

        # -- combien de poteaux hauts 
        label = QLabel("How many pillars")
        layout.addWidget(label)

        global haut_cbm
        haut_cbm = QSpinBox(self)
        haut_cbm.setRange(1, 10) # set la range
        haut_cbm.setValue(5) # valeur par défaut
        layout.addWidget(haut_cbm)

        # -- gap poteaux haut
        label = QLabel("Pillars Gap")
        layout.addWidget(label)

        global haut_gap
        haut_gap = QSpinBox(self)
        haut_gap.setRange(1, 6) # set la range
        haut_gap.setValue(3) # valeur par défaut
        layout.addWidget(haut_gap)

        # -- taille poteaux horizon
        label = QLabel("Horizontal pillar width (/10)")
        layout.addWidget(label)

        global horiz_width
        horiz_width = QSpinBox(self)
        horiz_width.setRange(1, 10) # set la range
        horiz_width.setValue(6) # valeur par défaut
        layout.addWidget(horiz_width)

         # -- taille gap poteaux horizon
        label = QLabel("Horizontal pillar gap")
        layout.addWidget(label)

        global horiz_gap
        horiz_gap = QSpinBox(self)
        horiz_gap.setRange(1, 6) # set la range
        horiz_gap.setValue(3) # valeur par défaut
        layout.addWidget(horiz_gap)

        # -- cbm de poteaux horizon
        label = QLabel("How many Horizontal pillar")
        layout.addWidget(label)

        global horiz_cbm
        horiz_cbm = QSpinBox(self)
        horiz_cbm.setRange(1, 5) # set la range
        horiz_cbm.setValue(2) # valeur par défaut
        layout.addWidget(horiz_cbm)
 
        button = QPushButton(self)
        button.setText("Generate Fence")
        layout.addWidget(button)
        button.clicked.connect(self.on_click)
   
    def on_click(self):
        cmds.delete(cmds.ls("cube_*", type="transform"))

        # cubes spread horizontal
        for i in range(haut_cbm.value()):
            cube = cmds.polyCube(
                name=f"cube_{i}",
                width=haut_largeur.value() / 10, # taille haut
                height=haut_longueur.value(), # longueur haut
                depth=haut_largeur.value() / 10
            )[0]

            cmds.move(i * haut_gap.value(), haut_longueur.value() / 2, 0, cube)

        # cubes spread vertical
        for i in range(horiz_cbm.value()):
            cube = cmds.polyCube(
                name=f"cube_{i}",
                width=((haut_largeur.value() / 10 ) * haut_cbm.value() + ((haut_gap.value()) * haut_cbm.value())) - 1,
                height=horiz_width.value() / 10,
                depth=horiz_width.value() / 10
            )[0]

            cmds.move((haut_gap.value() * 3 - 3 ) * (haut_cbm.value() / 4), i * horiz_gap.value() + 1.5, 0, cube)
   
 
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()

## params
# poteaux
# - longueur
# - largeur
# - combien
# lignes
# - longueur
# - largeur