from tkinter import *
import os
from PIL import ImageTk, Image
import Graphique
from tkinter import ttk
import liste_ingrédient
class init:

    def __init__(self, fenetre):
        dico = {}
        with open(os.path.abspath(__file__).replace("liste_ingrédient.py", "recette_actuel.txt"), "r") as f:
            contenu = f.read()
            exec(contenu, dico)
        contenu = []
        for i in ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche", "Extra"]:
            for y in ["_midi_recette","_soir_recette"]:
                contenu.append(dico[i + y][1])
        liste = contenu


        chemin_actuel = os.path.abspath(__file__)
        self.recette = chemin_actuel.replace("liste_ingrédient.py", "recette.txt")
        recette_et_plat=[]
        dico = {"recette_et_plat": recette_et_plat}
        with open(self.recette) as f:
            contenu = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â").replace("Fâte", "Fête")
            exec(contenu, dico)
        self.recette_et_plat = dico["recette_et_plat"]
        triage = []
        verif_sur = 1
        for nv_recette in range(len(self.recette_et_plat)):
               verif1 = 0
               for verif in liste:
                    if verif == self.recette_et_plat[nv_recette][0]:
                         verif1 +=1
               if verif1 >= verif_sur:
                    triage.append(self.recette_et_plat[nv_recette]) 
        self.liste_des_ingrédient = Label(fenetre, bg = "#d1fff7", height= 26, width= 38, text = triage)
        self.liste_des_ingrédient.place(x= 650, y = 110)

    def actualiser(self, fenetre):
        with open(os.path.abspath(__file__).replace("liste_ingrédient.py", "recette_actuel.txt"), "r") as f:
            contenu = f.read()
        self.liste_des_ingrédient = Label(fenetre, bg = "#d1fff7", height= 26, width= 38, text = contenu)
        self.liste_des_ingrédient.place(x= 650, y = 110)