from tkinter import *
import os
from PIL import ImageTk, Image
import Graphique, liste_ingrédient
from tkinter import ttk
fenetre = Tk()
fenetre.geometry("950x540")
chemin_actuel = os.path.abspath(__file__)
fenetre.iconbitmap(chemin_actuel.replace("Code.py", "Menu.ico"))
class code:
    def __init__(self):
        self.fenetre = fenetre
        chemin_actuel = os.path.abspath(__file__)
        self.recette = chemin_actuel.replace("Code.py", "recette.txt")
        recette_et_plat=[]
        dico = {"recette_et_plat": recette_et_plat}
        with open(self.recette) as f:
            contenu = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â").replace("Fâte", "Fête")
            exec(contenu, dico)
        self.recette_et_plat = dico["recette_et_plat"]

        self.menu_principal()

    def changer_de_menu(self):
        self.objet.destroy()

    def menu_principal(self):
        self.objet = Frame(fenetre)
        self.objet.pack(expand= YES)
        self.liste_des_ingré = liste_ingrédient.init(fenetre)
        self.fond = Graphique.graphisme.fond_écran(self.objet)
        self.Lundi = Graphique.graphisme.Menu.Lundi(self, self.objet, coef = 11, x= 0, y =0, mode = 1)
        self.Mardi = Graphique.graphisme.Menu.Mardi(self, self.objet, coef = 11, x= 1, y =0, mode = 1 )
        self.mercredi = Graphique.graphisme.Menu.Mercredi(self, self.objet, coef = 11, x= 2, y =0, mode = 1 )
        self.jeudi = Graphique.graphisme.Menu.Jeudi(self, self.objet, coef = 11, x= 3, y =0, mode = 1 )
        self.vendredi = Graphique.graphisme.Menu.Vendredi(self, self.objet, coef = 11, x= 0, y =2, mode = 1 )
        self.samedi = Graphique.graphisme.Menu.Samedi(self, self.objet, coef = 11, x= 1, y =2, mode = 1)
        self.dimanche = Graphique.graphisme.Menu.Dimanche(self, self.objet, coef = 11, x= 2, y =2 , mode = 1)
        self.Extra = Graphique.graphisme.Menu.Extra(self, self.objet, coef = 11, x= 3, y =2 , mode = 1)
        
    def retourmenuprin(self):
        self.changer_de_menu()
        self.menu_principal()

    def add_recette(self, jour = "a"):
        self.objet.destroy()
        self.objet = Frame(fenetre)
        self.objet.pack(expand= YES)
        self.fond = Graphique.graphisme.fond_écran(self.objet, mode = 2)
        self.bouton_ajouter = Graphique.graphisme.bouton_ajouter(self.objet, 900,55)
        self.bouton_trier= Graphique.graphisme.bouton_trier(self.objet, 900 ,90, self)
        self.boutton_aléa = Graphique.graphisme.bouton_aléa(self.objet, 900, 125, self)
        self.boutton_recherche = Graphique.graphisme.Entry_recherche(self.objet, 580, 45, self)
        self.jour = jour
        match jour[0]:
              case "Lundi":
                    self.Lundi = Graphique.graphisme.Menu.Lundi(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)
              
              case "Mardi":
                    self.Mardi = Graphique.graphisme.Menu.Mardi(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)
              
              case "Mercredi":
                    self.Mercredi = Graphique.graphisme.Menu.Mercredi(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)
        
              case "Jeudi":
                    self.Jeudi = Graphique.graphisme.Menu.Jeudi(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)

              case "Vendredi":
                    self.Vendredi = Graphique.graphisme.Menu.Vendredi(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)
              
              case "Samedi":
                    self.Samedi = Graphique.graphisme.Menu.Samedi(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)
              
              case "Dimanche":
                    self.Samedi = Graphique.graphisme.Menu.Dimanche(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)
              
              case "Extra":
                    self.Samedi = Graphique.graphisme.Menu.Extra(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)
              
                    
        
        
        self.retour = Graphique.graphisme.bouton_retour(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)
        self.position_recette_compteur = len(self.recette_et_plat) if len(self.recette_et_plat) < 16 else 16
        self.position_recette_compteur_avant = 0 
        y=68
        self.memoire = []
        for y2 in range(0,self.position_recette_compteur, 4):
              compteur = 580
              for x in range(4):
                
                try:
                        nom_de_la_recette = self.recette_et_plat[y2+x][0]
                        image_du_plat = self.recette_et_plat[y2+x][2][0]
                        immage = Graphique.graphisme.menu_recette(instance=self, fenetre=self.objet, coef = 2,x= compteur, y =y, image = image_du_plat, nom =nom_de_la_recette, jour = jour)
                        compteur = compteur + 75
                except:
                          break
              y += 110
        def suivant(self):
                self.position_recette_compteur = len(self.recette_et_plat) if len(self.recette_et_plat) < self.position_recette_compteur + 16 else self.position_recette_compteur + 16
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
                                nom_de_la_recette = self.recette_et_plat[y2+x][0]
                                image_du_plat = self.recette_et_plat[y2+x][2][0]
                                immage = Graphique.graphisme.menu_recette(instance=self, fenetre=self.objet, coef = 2,x= compteur, y =y, image = image_du_plat, nom =nom_de_la_recette, jour = jour)
                                compteur = compteur + 75
                           except:
                                break
                        y += 110
        self.btn_suivant = Button(fenetre, text = '→', font = ("Comic Sans MS", "20"), bd =0, bg = "light blue", activebackground= "blue", command = lambda : suivant(self))
        self.btn_suivant.place(x=900,y=288)
        fenetre.bind("<Right>", lambda event:suivant(self))
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
                                nom_de_la_recette = self.recette_et_plat[y2+x][0]
                                image_du_plat = self.recette_et_plat[y2+x][2][0]
                                immage = Graphique.graphisme.menu_recette(instance=self, fenetre=self.objet, coef = 2,x= compteur, y =y, image = image_du_plat, nom =nom_de_la_recette, jour = jour)
                                compteur = compteur + 75
                             except:
                                break
                        y += 110
        self.btn_arriere = Button(fenetre, text = '←', font = ("Comic Sans MS", "20"), bd =0, bg = "light blue", activebackground= "blue", command = lambda : arriere(self))
        self.btn_arriere.place(x=500,y=288)
        fenetre.bind("<Left>", lambda event:arriere(self))

        

    ####################################################################################################
    #                                                                                                  #
    #  MENU JOUR                            MENU JOUR                                        MENU JOUR #
    #                                                                                                  #
    ####################################################################################################

    def Menu_lundi(self):
                self.changer_de_menu()
                self.objet = Frame(fenetre)
                self.objet.pack(expand= YES)
                self.fond = Graphique.graphisme.fond_écran(self.objet)
                self.Lundi = Graphique.graphisme.Menu.Lundi(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)
                self.retour = Graphique.graphisme.bouton_retour(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)

    def Menu_Mardi(self): 
            self.changer_de_menu()
            self.objet = Frame(fenetre)
            self.objet.pack(expand= YES)
            self.fond = Graphique.graphisme.fond_écran(self.objet)
            self.Lundi = Graphique.graphisme.Menu.Mardi(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)
            self.retour = Graphique.graphisme.bouton_retour(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)

    def Menu_Mercredi(self): 
            self.changer_de_menu()
            self.objet = Frame(fenetre)
            self.objet.pack(expand= YES)
            self.fond = Graphique.graphisme.fond_écran(self.objet)
            self.Lundi = Graphique.graphisme.Menu.Mercredi(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)
            self.retour = Graphique.graphisme.bouton_retour(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)

    def Menu_Jeudi(self): 
            self.changer_de_menu()
            self.objet = Frame(fenetre)
            self.objet.pack(expand= YES)
            self.fond = Graphique.graphisme.fond_écran(self.objet)
            self.Lundi = Graphique.graphisme.Menu.Jeudi(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)
            self.retour = Graphique.graphisme.bouton_retour(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)
            
    def Menu_Vendredi(self): 
            self.changer_de_menu()
            self.objet = Frame(fenetre)
            self.objet.pack(expand= YES)
            self.fond = Graphique.graphisme.fond_écran(self.objet)
            self.Lundi = Graphique.graphisme.Menu.Vendredi(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)
            self.retour = Graphique.graphisme.bouton_retour(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)

    def Menu_Samedi(self): 
            self.changer_de_menu()
            self.objet = Frame(fenetre)
            self.objet.pack(expand= YES)
            self.fond = Graphique.graphisme.fond_écran(self.objet)
            self.Lundi = Graphique.graphisme.Menu.Samedi(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)
            self.retour = Graphique.graphisme.bouton_retour(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)

    def Menu_Dimanche(self): 
            self.changer_de_menu()
            self.objet = Frame(fenetre)
            self.objet.pack(expand= YES)
            self.fond = Graphique.graphisme.fond_écran(self.objet)
            self.Lundi = Graphique.graphisme.Menu.Dimanche(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)
            self.retour = Graphique.graphisme.bouton_retour(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)

    def Menu_Extra(self): 
            self.changer_de_menu()
            self.objet = Frame(fenetre)
            self.objet.pack(expand= YES)
            self.fond = Graphique.graphisme.fond_écran(self.objet)
            self.Lundi = Graphique.graphisme.Menu.Extra(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)
            self.retour = Graphique.graphisme.bouton_retour(instance=self, fenetre=self.objet, coef = 4.5, x= 1, y =-0.75, mode = 2)

    ####################################################################################################
    #                                                                                                  #
    #  FIN DE MENU JOUR                         FIN DE MENU JOUR                      FIN DE MENU JOUR #
    #                                                                                                  #
    ####################################################################################################




run = code()
fenetre.mainloop()

