from tkinter import *
import os
from PIL import ImageTk, Image
import Graphique, menu_recette
from tkinter import ttk
import random

class init:

    def affichage_de_recette_précise(self, type,instance_code_prin):
        chemin_actuel = os.path.abspath(__file__)
        self.recette = chemin_actuel.replace("menu_recette.py", "recette.txt")
        recette_et_plat=[]
        dico = {"recette_et_plat": recette_et_plat}
        with open(self.recette) as f:
            contenu = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â").replace("Fâte", "Fête")
            exec(contenu, dico)
        self.recette_et_plat = dico["recette_et_plat"]
        triage = []
        verif_sur = len(type)
        for nv_recette in range(len(self.recette_et_plat)):
               verif1 = 0
               for verif in type:
                    if verif in self.recette_et_plat[nv_recette][2]:
                         verif1 +=1
               if verif1 == verif_sur:
                    triage.append(self.recette_et_plat[nv_recette])    
        menu_recette.init.affichage(self, triage,instance_code_prin)
     
    def affichage_de_recette_précise_aléa(self, type,instance_code_prin):
        chemin_actuel = os.path.abspath(__file__)
        self.recette = chemin_actuel.replace("menu_recette.py", "recette.txt")
        recette_et_plat=[]
        dico = {"recette_et_plat": recette_et_plat}
        with open(self.recette) as f:
            contenu = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â").replace("Fâte", "Fête")
            exec(contenu, dico)
        self.recette_et_plat = dico["recette_et_plat"]
        triage = []
        verif_sur = len(type)
        for nv_recette in range(len(self.recette_et_plat)):
               verif1 = 0
               for verif in type:
                    if verif in self.recette_et_plat[nv_recette][2]:
                         verif1 +=1
               if verif1 == verif_sur:
                    triage.append(self.recette_et_plat[nv_recette])  
        triage = [triage[random.randint(0, len(triage))]  ]
        menu_recette.init.affichage(self, triage,instance_code_prin)
    
    def affichage_avec_nom(self,nom,instance_code_prin):
        chemin_actuel = os.path.abspath(__file__)
        self.recette = chemin_actuel.replace("menu_recette.py", "recette.txt")
        recette_et_plat=[]
        dico = {"recette_et_plat": recette_et_plat}
        with open(self.recette) as f:
            contenu = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â").replace("Fâte", "Fête")
            exec(contenu, dico)
        self.recette_et_plat = dico["recette_et_plat"]
        triage = []
        nom = nom.lower().split(" ")
        verif_sur = len(nom)
        for nv_recette in range(len(self.recette_et_plat)):
               verif1 = 0
               for verif in nom:
                    if verif in self.recette_et_plat[nv_recette][0].lower().replace("\n", " ").split(" "):
                         verif1 +=1
               if verif1 == verif_sur:
                    triage.append(self.recette_et_plat[nv_recette]) 
        for etape_intermediaire in triage:
               del self.recette_et_plat[self.recette_et_plat.index(etape_intermediaire)]

        verif_sur = len(nom)
        for nv_recette in range(len(self.recette_et_plat)):
               verif1 = 0
               for verif in nom:
                    for i in range(len(self.recette_et_plat[nv_recette][1][0])):
                         self.recette_et_plat[nv_recette][1][0][i]= self.recette_et_plat[nv_recette][1][0][i].lower()
                    if verif in self.recette_et_plat[nv_recette][1][0]:
                         verif1 +=1
               if verif1 == verif_sur:
                    triage.append(self.recette_et_plat[nv_recette]) 

        menu_recette.init.affichage(self, triage,instance_code_prin)
         
    def affichage(self, liste,instance_code_prin):
          
          self.liste=liste
          self.position_recette_compteur = len(liste) if len(liste) < 16 else 16
          self.position_recette_compteur_avant = 0 
          y=68
          self.memoire = []
          for y2 in range(0,self.position_recette_compteur, 4):
               compteur = 580
               for x in range(4):
                    
                    try:     
                         nom_de_la_recette = self.liste[y2+x][0]
                         image_du_plat = self.liste[y2+x][2][0]
                         immage = Graphique.graphisme.menu_recette(instance=instance_code_prin, fenetre=instance_code_prin.objet, coef = 2,x= compteur, y =y, image = image_du_plat, nom =nom_de_la_recette, jour = instance_code_prin.jour)
                         compteur = compteur + 75
                    except:
                          break
               y += 110
          def suivant(self):
                    self.position_recette_compteur = len(self.liste) if len(self.liste) < self.position_recette_compteur + 16 else self.position_recette_compteur + 16
                    self.position_recette_compteur_avant = self.position_recette_compteur - 16 if not self.position_recette_compteur - 16 <0 else 0
                    for widget in self.memoire:
                         widget[0].destroy()
                         widget[1].destroy()
                    y=68
                    self.memoire = []
                    for y2 in range(self.position_recette_compteur_avant,self.position_recette_compteur, 4):
                         compteur = 580
                         for x in range(4):
                              try:
                                   nom_de_la_recette = self.liste[y2+x][0]
                                   image_du_plat = self.liste[y2+x][2][0]
                                   immage = Graphique.graphisme.menu_recette(instance=instance_code_prin, fenetre=instance_code_prin.objet, coef = 2,x= compteur, y =y, image = image_du_plat, nom =nom_de_la_recette, jour = instance_code_prin.jour)
                                   compteur = compteur + 75
                              except:
                                    break
                         y += 110
          self.btn_suivant = Button(instance_code_prin.fenetre, text = '→', font = ("Comic Sans MS", "20"), bd =0, bg = "light blue", activebackground= "blue", command = lambda : suivant(self))
          self.btn_suivant.place(x=900,y=288)
          instance_code_prin.fenetre.bind("<Right>", lambda event:suivant(self))
          def arriere(self):
                    self.position_recette_compteur = self.position_recette_compteur - 16 if 16 < self.position_recette_compteur - 16  else 16
                    self.position_recette_compteur_avant = self.position_recette_compteur - 16 if not self.position_recette_compteur - 16 <0 else 0
                    for widget in self.memoire:
                         widget[0].destroy()
                         widget[1].destroy()
                    y=68
                    self.memoire = []
                    for y2 in range(self.position_recette_compteur_avant,self.position_recette_compteur, 4):
                         compteur = 580
                         for x in range(4):
                              try:
                                   nom_de_la_recette = self.liste[y2+x][0]
                                   image_du_plat = self.liste[y2+x][2][0]
                                   immage = Graphique.graphisme.menu_recette(instance=instance_code_prin, fenetre=instance_code_prin.objet, coef = 2,x= compteur, y =y, image = image_du_plat, nom =nom_de_la_recette, jour = instance_code_prin.jour)
                                   compteur = compteur + 75
                              except:
                                   break
                         y += 110
          self.btn_arriere = Button(instance_code_prin.fenetre, text = '←', font = ("Comic Sans MS", "20"), bd =0, bg = "light blue", activebackground= "blue", command = lambda : arriere(self))
          self.btn_arriere.place(x=500,y=288)
          instance_code_prin.fenetre.bind("<Left>", lambda event:arriere(self))
                              
                              