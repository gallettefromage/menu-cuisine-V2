from tkinter import *
import os
from PIL import ImageTk, Image
import Graphique
from tkinter import ttk
import Recherche_btn, menu_recette
class init:
    def __init__(self, fenetre, instance, recherche):
        data = recherche.get("1.0", END)[:-1].replace("\n", "")
        print(data)
        recherche.delete('1.0', END)
        for widget in fenetre.winfo_children():
                     if isinstance(widget, Button):
                            largeur = widget.winfo_width()
                            if largeur == 66:
                                widget.destroy()
                            
                     if isinstance(widget, Label):
                            taille = widget.cget("font")
                            if taille.replace("{"+"} ","" ) == "8":
                                widget.destroy()
        instance.btn_arriere.destroy()
        instance.btn_suivant.destroy()
        menu_recette.init.affichage_avec_nom(self, data, instance)