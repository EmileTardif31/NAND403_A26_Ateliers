import sys
import json
import os

fichier = "drinks.json"

if os.path.exists(fichier):
    print("Fichier valide.")
else:
    print("Ce fichier est introuvable ou n'existe pas.")
    exit()

with open("drinks.json", "r", encoding="utf-8") as small_fichier:
    donnees_small = json.load(small_fichier)

from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

app = QApplication(sys.argv)

tableau = QTableWidget()
tableau_choisi = donnees_small

tableau.setRowCount(len(tableau_choisi))
tableau.setColumnCount(len(tableau_choisi[0]))

tableau.setHorizontalHeaderLabels(tableau_choisi[0].keys())

for ligne, i in enumerate(tableau_choisi):            
    for colonne, k in enumerate(i):                    
        tableau.setItem(ligne, colonne, QTableWidgetItem(str(i[k])))

sys.exit(app.exec())