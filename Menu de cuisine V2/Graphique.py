from tkinter import *
import os
from PIL import ImageTk, Image
import Graphique
from tkinter import ttk
import Création_recette, Trier_recette, button_aléa, Recherche_btn
class graphisme:



    class fond_écran:
        def __init__(self, fenetre, mode = 1):
            if mode ==1:
                self.fenetre = fenetre
                chemin_actuel = os.path.abspath(__file__)
                chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Menu.png")
                image = Image.open(chemin_actuel)
                self.image = ImageTk.PhotoImage(image)
                self.fond = Label(self.fenetre, image = self.image)
                self.fond.image = self.image 
                self.fond.pack(expand= YES)
            elif mode ==2:
                self.fond_recette(fenetre)


        def fond_recette(self, fenetre):
                self.fenetre = fenetre
                chemin_actuel = os.path.abspath(__file__)
                chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Menu_Recette.png")
                image = Image.open(chemin_actuel)
                self.image = ImageTk.PhotoImage(image)
                self.fond = Label(self.fenetre, image = self.image)
                self.fond.image = self.image 
                self.fond.pack(expand= YES)  
    

    class bouton_retour:
        def __init__(self, instance, fenetre, coef = 11, x=1 , y=1, mode = 1):
            self.fenetre = fenetre
            chemin_actuel = os.path.abspath(__file__)
            chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Bouton_retour.png")
            image = Image.open(chemin_actuel)
            image = image.resize((20, 20), Image.LANCZOS)
            self.image = ImageTk.PhotoImage(image)
            self.bouton = Button(self.fenetre, image = self.image, bg = "white", activebackground= "white", bd =0, command = instance.retourmenuprin)
            self.bouton.image = self.image 
            self.bouton.place(x= 165, y=42)

    class bouton_ajouter:
        def __init__(self, fenetre, x , y):
            chemin_actuel = os.path.abspath(__file__)
            chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\ajouter_recette.png")
            image = Image.open(chemin_actuel)
            image = image.resize((20, 20), Image.LANCZOS)
            image = ImageTk.PhotoImage(image)
            bouton = Button(fenetre, image = image, bg = "white", activebackground= "white", bd =2, command = lambda : self.ajouter_une_recette(fenetre))
            bouton.image = image 
            bouton.place(x= x, y=y)

        class ajouter_une_recette:
            def __init__(self, fenetre):
                Création_recette.init(fenetre)
        
    class bouton_trier:
        def __init__(self, fenetre, x, y, instance_code_prin):
            chemin_actuel = os.path.abspath(__file__)
            chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Trier.png")
            image = Image.open(chemin_actuel)
            image = image.resize((20, 20), Image.LANCZOS)
            image = ImageTk.PhotoImage(image)
            bouton = Button(fenetre, image = image, bg = "white", activebackground= "white", bd =2, command = lambda :faire_trier(fenetre, instance_code_prin))
            bouton.image = image 
            bouton.place(x= x, y=y)
            class faire_trier:
                def __init__(self, fenetre, instance_code_prin):
                    Trier_recette.init(fenetre,instance_code_prin)
                
    class bouton_aléa:
        def __init__(self, fenetre, x, y, instance_code_prin):
            chemin_actuel = os.path.abspath(__file__)
            chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Aléa.png")
            image = Image.open(chemin_actuel)
            image = image.resize((20, 20), Image.LANCZOS)
            image = ImageTk.PhotoImage(image)
            bouton = Button(fenetre, image = image, bg = "white", activebackground= "white", bd =2, command = lambda :faire_aléa(fenetre, instance_code_prin))
            bouton.image = image 
            bouton.place(x= x, y=y)
            class faire_aléa:
                def __init__(self, fenetre, instance_code_prin):
                    button_aléa.init(fenetre,instance_code_prin)

    class Entry_recherche:
        def __init__(self, fenetre, x, y, instance_code_prin):
            bouton = Text(fenetre, bg = "white", bd =2, height=1, width= 20)
            bouton.place(x= x, y=y)
            class recherche:
                def __init__(self, fenetre, instance_code_prin):
                    Recherche_btn.init(fenetre,instance_code_prin, bouton)
            bouton.bind("<Return>", lambda event:recherche(fenetre, instance_code_prin))


    class Menu:
        class Lundi:
            def __init__(self, instance, fenetre, coef = 11, x=1 , y=1, mode = 1):
                if mode == 1:
                    self.fenetre = fenetre
                    chemin_actuel = os.path.abspath(__file__)
                    chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Lundi.png")
                    image = Image.open(chemin_actuel)
                    image = image.resize((int(1587//coef//1), int(2245//coef//1)), Image.LANCZOS)
                    self.image = ImageTk.PhotoImage(image)
                    self.menu_Lundi = Button(self.fenetre, image = self.image, activebackground= "magenta", bd =0, command = instance.Menu_lundi)
                    self.menu_Lundi.image = self.image 
                    self.menu_Lundi.place(x= 40 + x *100, y=100 + y *105)
                    self.Recette.recette_midi(self, instance, fenetre=fenetre, coef = 11, x=0.5 , y=0.6, te = "9",x2= 88 + 0.5 *100, y2=100 + 0.6 *105)
                    self.Recette.recette_soir(self, instance, fenetre=fenetre, coef = 11, x=0.5 , y=1.325, te = "9",x2= 88 + 0.5 *100, y2=100 + 1.325 *105)
                elif mode == 2:
                    self.Menu_avec_lundi_en_grand( instance, fenetre, coef = coef, x =x , y =y) 

            def Menu_avec_lundi_en_grand(self, instance, fenetre, coef = 11, x=1 , y=1):
                self.fenetre = fenetre
                chemin_actuel = os.path.abspath(__file__)
                chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Lundi.png")
                image = Image.open(chemin_actuel)
                image = image.resize((int(1587//coef//1), int(2245//coef//1)), Image.LANCZOS)
                self.image = ImageTk.PhotoImage(image)
                self.menu_Lundi = Label(self.fenetre, image = self.image, bd =0)
                self.menu_Lundi.image = self.image 
                self.menu_Lundi.place(x= 40 + x *100, y=100 + y *105)
                self.Recette.recette_midi(self, instance, fenetre=fenetre, coef = 6, x=2.3 , y=0.8, te = "20",x2=  120+2.3 *100, y2=100 + 0.8 *105)
                self.Recette.recette_soir(self, instance, fenetre=fenetre, coef = 6, x=2.3 , y=2.6, te = "20",x2=  120+2.3 *100, y2=100 + 2.6 *105)

            class Recette:
                def recette_midi(self, instance, fenetre, coef = 11, x=1 , y=1, te = 1, y2 = 1, x2 = 1):
                        fichier = os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt")
                        dico = {}
                        with open(fichier, "r") as f:
                            contenue = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â")
                            exec(contenue, dico)
                        image = dico['Lundi_midi_recette'][0]
                        nom = dico["Lundi_midi_recette"][1]
                        self.fenetre = fenetre
                        chemin = os.path.abspath(__file__).replace("Graphique.py", "icone_recette\\"+image+".png" )
                        image = Image.open(chemin)
                        image = image.resize((int(500//coef//1), int(500//coef//1)), Image.LANCZOS)
                        self.image = ImageTk.PhotoImage(image)
                        self.menu_Lundi_midi = Button(self.fenetre, image = self.image, bd =0, bg = "#ECFFFC", command = lambda: instance.add_recette(jour = ["Lundi", "midi"]))
                        tooltip = Button(fenetre, text=nom, font = ("",te), bd=0, bg="#ECFFFC", command = lambda : instance.add_recette(jour = ["Lundi", "midi"]))

                        def enter(event):
                            tooltip.place(x= x2, y=y2)
                            tooltip.lift()
                            
                        def leave(event):
                            tooltip.place_forget()
                        self.menu_Lundi_midi.bind('<Enter>', enter)
                        self.menu_Lundi_midi.bind('<Leave>', leave)
                        self.menu_Lundi_midi.image = self.image 
                        self.menu_Lundi_midi.place(x= 40 + x *100, y=100 + y *105)
                
                def recette_soir(self, instance, fenetre, coef = 11, x=1 , y=1, te = 1, y2 = 1, x2 = 1):
                        fichier = os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt")
                        dico = {}
                        with open(fichier, "r") as f:
                            contenue = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â")
                            exec(contenue, dico)
                        image = dico['Lundi_soir_recette'][0]
                        nom = dico["Lundi_soir_recette"][1]
                        self.fenetre = fenetre
                        chemin = os.path.abspath(__file__).replace("Graphique.py", "icone_recette\\"+image+".png" )
                        image = Image.open(chemin)
                        image = image.resize((int(500//coef//1), int(500//coef//1)), Image.LANCZOS)
                        self.image = ImageTk.PhotoImage(image)
                        self.menu_Lundi_soir = Button(self.fenetre, image = self.image, bd =0, bg = "#ECFFFC", command = lambda: instance.add_recette(jour = ["Lundi", "soir"]))
                        tooltip = Button(fenetre, text=nom, font = ("",te), bd=0, bg="#ECFFFC", command = lambda : instance.add_recette(jour = ["Lundi", "soir"]))

                        def enter(event):
                            tooltip.place(x= x2, y=y2)
                            tooltip.lift()
                            
                        def leave(event):
                            tooltip.place_forget()
                        self.menu_Lundi_soir.bind('<Enter>', enter)
                        self.menu_Lundi_soir.bind('<Leave>', leave)
                        self.menu_Lundi_soir.image = self.image 
                        self.menu_Lundi_soir.place(x= 40 + x *100, y=100 + y *105)

        class Mardi:
            def __init__(self, instance, fenetre, coef = 11, x=1 , y=1, mode = 1):
                if mode == 1:
                    self.fenetre = fenetre
                    chemin_actuel = os.path.abspath(__file__)
                    chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Mardi.png")
                    image = Image.open(chemin_actuel)
                    image = image.resize((int(1587//coef//1), int(2245//coef//1)), Image.LANCZOS)
                    self.image = ImageTk.PhotoImage(image)
                    self.menu_Mardi = Button(self.fenetre, image = self.image, activebackground= "magenta", bd =0, command = instance.Menu_Mardi)
                    self.menu_Mardi.image = self.image 
                    self.menu_Mardi.place(x=40 + x *100 + 50*x, y=100 + y *105)
                    self.Recette.recette_midi(self, instance, fenetre=fenetre, coef = 11, x=2 , y=0.6, te = "9",x2= 88 + 2 *100, y2=100 + 0.6 *105)
                    self.Recette.recette_soir(self, instance, fenetre=fenetre, coef = 11, x=2 , y=1.325, te = "9",x2= 88 + 2 *100, y2=100 + 1.325 *105)
                elif mode == 2:
                    self.Menu_avec_mardi_en_grand( instance, fenetre, coef = coef, x =x , y =y) 

            def Menu_avec_mardi_en_grand(self, instance, fenetre, coef = 11, x=1 , y=1):
                self.fenetre = fenetre
                chemin_actuel = os.path.abspath(__file__)
                chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Mardi.png")
                image = Image.open(chemin_actuel)
                image = image.resize((int(1587//coef//1), int(2245//coef//1)), Image.LANCZOS)
                self.image = ImageTk.PhotoImage(image)
                self.menu_Mardi = Label(self.fenetre, image = self.image, bd =0)
                self.menu_Mardi.image = self.image 
                self.menu_Mardi.place(x= 40 + x *100, y=100 + y *105)
                self.Recette.recette_midi(self, instance, fenetre=fenetre, coef = 6, x=2.3 , y=0.8, te = "20",x2=  120+2.3 *100, y2=100 + 0.8 *105)
                self.Recette.recette_soir(self, instance, fenetre=fenetre, coef = 6, x=2.3 , y=2.6, te = "20",x2=  120+2.3 *100, y2=100 + 2.6 *105)

            class Recette:
                def recette_midi(self, instance, fenetre, coef = 11, x=1 , y=1, te = 1, y2 = 1, x2 = 1):
                        fichier = os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt")
                        dico = {}
                        with open(fichier, "r") as f:
                            contenue = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â")
                            exec(contenue, dico)
                        image = dico['Mardi_midi_recette'][0]
                        nom = dico["Mardi_midi_recette"][1]
                        self.fenetre = fenetre
                        chemin = os.path.abspath(__file__).replace("Graphique.py", "icone_recette\\"+image+".png" )
                        image = Image.open(chemin)
                        image = image.resize((int(500//coef//1), int(500//coef//1)), Image.LANCZOS)
                        self.image = ImageTk.PhotoImage(image)
                        self.menu_Mardi_midi = Button(self.fenetre, image = self.image, bd =0, bg = "#ECFFFC", command = lambda: instance.add_recette(jour = ["Mardi", "midi"]))
                        tooltip = Button(fenetre, text=nom, font = ("",te), bd=0, bg="#ECFFFC", command = lambda : instance.add_recette(jour = ["Mardi", "midi"]))

                        def enter(event):
                            tooltip.place(x= x2, y=y2)
                            tooltip.lift()
                            
                        def leave(event):
                            tooltip.place_forget()
                        self.menu_Mardi_midi.bind('<Enter>', enter)
                        self.menu_Mardi_midi.bind('<Leave>', leave)
                        self.menu_Mardi_midi.image = self.image 
                        self.menu_Mardi_midi.place(x= 40 + x *100, y=100 + y *105)
                
                def recette_soir(self, instance, fenetre, coef = 11, x=1 , y=1, te = 1, y2 = 1, x2 = 1):
                        fichier = os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt")
                        dico = {}
                        with open(fichier, "r") as f:
                            contenue = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â")
                            exec(contenue, dico)
                        image = dico['Mardi_soir_recette'][0]
                        nom = dico["Mardi_soir_recette"][1]
                        self.fenetre = fenetre
                        chemin = os.path.abspath(__file__).replace("Graphique.py", "icone_recette\\"+image+".png" )
                        image = Image.open(chemin)
                        image = image.resize((int(500//coef//1), int(500//coef//1)), Image.LANCZOS)
                        self.image = ImageTk.PhotoImage(image)
                        self.menu_Mardi_soir = Button(self.fenetre, image = self.image, bd =0, bg = "#ECFFFC", command = lambda: instance.add_recette(jour = ["Mardi", "soir"]))
                        tooltip = Button(fenetre, text=nom, font = ("",te), bd=0, bg="#ECFFFC", command = lambda : instance.add_recette(jour = ["Mardi", "soir"]))

                        def enter(event):
                            tooltip.place(x= x2, y=y2)
                            tooltip.lift()
                            
                        def leave(event):
                            tooltip.place_forget()
                        self.menu_Mardi_soir.bind('<Enter>', enter)
                        self.menu_Mardi_soir.bind('<Leave>', leave)
                        self.menu_Mardi_soir.image = self.image 
                        self.menu_Mardi_soir.place(x= 40 + x *100, y=100 + y *105)
            
        class Mercredi:
            def __init__(self, instance, fenetre, coef = 11, x=1 , y=1, mode = 1):
                if mode == 1:
                    self.fenetre = fenetre
                    chemin_actuel = os.path.abspath(__file__)
                    chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Mercredi.png")
                    image = Image.open(chemin_actuel)
                    image = image.resize((int(1587//coef//1), int(2245//coef//1)), Image.LANCZOS)
                    self.image = ImageTk.PhotoImage(image)
                    self.menu_Mercredi = Button(self.fenetre, image = self.image, activebackground= "magenta", bd =0, command = instance.Menu_Mercredi)
                    self.menu_Mercredi.image = self.image 
                    self.menu_Mercredi.place(x=40 + x *100 + 50*x, y=100 + y *105)
                    self.Recette.recette_midi(self, instance, fenetre=fenetre, coef = 11, x=3.5 , y=0.6, te = "9",x2= 88 + 3.5 *100, y2=100 + 0.6 *105)
                    self.Recette.recette_soir(self, instance, fenetre=fenetre, coef = 11, x=3.5 , y=1.325, te = "9",x2= 88 + 3.5 *100, y2=100 + 1.325 *105)
                elif mode == 2:
                    self.Menu_avec_mercredi_en_grand( instance, fenetre, coef = coef, x =x , y =y) 

            def Menu_avec_mercredi_en_grand(self, instance, fenetre, coef = 11, x=1 , y=1):
                self.fenetre = fenetre
                chemin_actuel = os.path.abspath(__file__)
                chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Mercredi.png")
                image = Image.open(chemin_actuel)
                image = image.resize((int(1587//coef//1), int(2245//coef//1)), Image.LANCZOS)
                self.image = ImageTk.PhotoImage(image)
                self.menu_Mercredi = Label(self.fenetre, image = self.image, bd =0)
                self.menu_Mercredi.image = self.image 
                self.menu_Mercredi.place(x= 40 + x *100, y=100 + y *105)
                self.Recette.recette_midi(self, instance, fenetre=fenetre, coef = 6, x=2.3 , y=0.8, te = "20",x2=  120+2.3 *100, y2=100 + 0.8 *105)
                self.Recette.recette_soir(self, instance, fenetre=fenetre, coef = 6, x=2.3 , y=2.6, te = "20",x2=  120+2.3 *100, y2=100 + 2.6 *105)

            class Recette:
                def recette_midi(self, instance, fenetre, coef = 11, x=1 , y=1, te = 1, y2 = 1, x2 = 1):
                        fichier = os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt")
                        dico = {}
                        with open(fichier, "r") as f:
                            contenue = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â")
                            exec(contenue, dico)
                        image = dico['Mercredi_midi_recette'][0]
                        nom = dico["Mercredi_midi_recette"][1]
                        self.fenetre = fenetre
                        chemin = os.path.abspath(__file__).replace("Graphique.py", "icone_recette\\"+image+".png" )
                        image = Image.open(chemin)
                        image = image.resize((int(500//coef//1), int(500//coef//1)), Image.LANCZOS)
                        self.image = ImageTk.PhotoImage(image)
                        self.menu_Mercredi_midi = Button(self.fenetre, image = self.image, bd =0, bg = "#ECFFFC", command = lambda: instance.add_recette(jour = ["Mercredi", "midi"]))
                        tooltip = Button(fenetre, text=nom, font = ("",te), bd=0, bg="#ECFFFC", command = lambda : instance.add_recette(jour = ["Mercredi", "midi"]))

                        def enter(event):
                            tooltip.place(x= x2, y=y2)
                            tooltip.lift()
                            
                        def leave(event):
                            tooltip.place_forget()
                        self.menu_Mercredi_midi.bind('<Enter>', enter)
                        self.menu_Mercredi_midi.bind('<Leave>', leave)
                        self.menu_Mercredi_midi.image = self.image 
                        self.menu_Mercredi_midi.place(x= 40 + x *100, y=100 + y *105)
                
                def recette_soir(self, instance, fenetre, coef = 11, x=1 , y=1, te = 1, y2 = 1, x2 = 1):
                        fichier = os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt")
                        dico = {}
                        with open(fichier, "r") as f:
                            contenue = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â")
                            exec(contenue, dico)
                        image = dico['Mercredi_soir_recette'][0]
                        nom = dico["Mercredi_soir_recette"][1]
                        self.fenetre = fenetre
                        chemin = os.path.abspath(__file__).replace("Graphique.py", "icone_recette\\"+image+".png" )
                        image = Image.open(chemin)
                        image = image.resize((int(500//coef//1), int(500//coef//1)), Image.LANCZOS)
                        self.image = ImageTk.PhotoImage(image)
                        self.menu_Mercredi_soir = Button(self.fenetre, image = self.image, bd =0, bg = "#ECFFFC", command = lambda: instance.add_recette(jour = ["Mercredi", "soir"]))
                        tooltip = Button(fenetre, text=nom, font = ("",te), bd=0, bg="#ECFFFC", command = lambda : instance.add_recette(jour = ["Mercredi", "soir"]))

                        def enter(event):
                            tooltip.place(x= x2, y=y2)
                            tooltip.lift()
                            
                        def leave(event):
                            tooltip.place_forget()
                        self.menu_Mercredi_soir.bind('<Enter>', enter)
                        self.menu_Mercredi_soir.bind('<Leave>', leave)
                        self.menu_Mercredi_soir.image = self.image 
                        self.menu_Mercredi_soir.place(x= 40 + x *100, y=100 + y *105)

        class Jeudi:
            def __init__(self, instance, fenetre, coef = 11, x=1 , y=1, mode = 1):
                if mode == 1:
                    self.fenetre = fenetre
                    chemin_actuel = os.path.abspath(__file__)
                    chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Jeudi.png")
                    image = Image.open(chemin_actuel)
                    image = image.resize((int(1587//coef//1), int(2245//coef//1)), Image.LANCZOS)
                    self.image = ImageTk.PhotoImage(image)
                    self.menu_Jeudi = Button(self.fenetre, image = self.image, activebackground= "magenta", bd =0, command = instance.Menu_Jeudi)
                    self.menu_Jeudi.image = self.image 
                    self.menu_Jeudi.place(x=40 + x *100 + 50*x, y=100 + y *105)
                    self.Recette.recette_midi(self, instance, fenetre=fenetre, coef = 11, x=5 , y=0.6, te = "9",x2= 88 + 5 *100, y2=100 + 0.6 *105)
                    self.Recette.recette_soir(self, instance, fenetre=fenetre, coef = 11, x=5 , y=1.325, te = "9",x2= 88 + 5 *100, y2=100 + 1.325 *105)
                elif mode == 2:
                    self.Menu_avec_jeudi_en_grand( instance, fenetre, coef = coef, x =x , y =y) 

            def Menu_avec_jeudi_en_grand(self, instance, fenetre, coef = 11, x=1 , y=1):
                self.fenetre = fenetre
                chemin_actuel = os.path.abspath(__file__)
                chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Jeudi.png")
                image = Image.open(chemin_actuel)
                image = image.resize((int(1587//coef//1), int(2245//coef//1)), Image.LANCZOS)
                self.image = ImageTk.PhotoImage(image)
                self.menu_Jeudi = Label(self.fenetre, image = self.image, bd =0)
                self.menu_Jeudi.image = self.image 
                self.menu_Jeudi.place(x= 40 + x *100, y=100 + y *105)
                self.Recette.recette_midi(self, instance, fenetre=fenetre, coef = 6, x=2.3 , y=0.8, te = "20",x2=  120+2.3 *100, y2=100 + 0.8 *105)
                self.Recette.recette_soir(self, instance, fenetre=fenetre, coef = 6, x=2.3 , y=2.6, te = "20",x2=  120+2.3 *100, y2=100 + 2.6 *105)

            class Recette:
                def recette_midi(self, instance, fenetre, coef = 11, x=1 , y=1, te = 1, y2 = 1, x2 = 1):
                        fichier = os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt")
                        dico = {}
                        with open(fichier, "r") as f:
                            contenue = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â")
                            exec(contenue, dico)
                        image = dico['Jeudi_midi_recette'][0]
                        nom = dico["Jeudi_midi_recette"][1]
                        self.fenetre = fenetre
                        chemin = os.path.abspath(__file__).replace("Graphique.py", "icone_recette\\"+image+".png" )
                        image = Image.open(chemin)
                        image = image.resize((int(500//coef//1), int(500//coef//1)), Image.LANCZOS)
                        self.image = ImageTk.PhotoImage(image)
                        self.menu_Jeudi_midi = Button(self.fenetre, image = self.image, bd =0, bg = "#ECFFFC", command = lambda: instance.add_recette(jour = ["Jeudi", "midi"]))
                        tooltip = Button(fenetre, text=nom, font = ("",te), bd=0, bg="#ECFFFC", command = lambda : instance.add_recette(jour = ["Jeudi", "midi"]))

                        def enter(event):
                            tooltip.place(x= x2, y=y2)
                            tooltip.lift()
                            
                        def leave(event):
                            tooltip.place_forget()
                        self.menu_Jeudi_midi.bind('<Enter>', enter)
                        self.menu_Jeudi_midi.bind('<Leave>', leave)
                        self.menu_Jeudi_midi.image = self.image 
                        self.menu_Jeudi_midi.place(x= 40 + x *100, y=100 + y *105)
                
                def recette_soir(self, instance, fenetre, coef = 11, x=1 , y=1, te = 1, y2 = 1, x2 = 1):
                        fichier = os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt")
                        dico = {}
                        with open(fichier, "r") as f:
                            contenue = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â")
                            exec(contenue, dico)
                        image = dico['Jeudi_soir_recette'][0]
                        nom = dico["Jeudi_soir_recette"][1]
                        self.fenetre = fenetre
                        chemin = os.path.abspath(__file__).replace("Graphique.py", "icone_recette\\"+image+".png" )
                        image = Image.open(chemin)
                        image = image.resize((int(500//coef//1), int(500//coef//1)), Image.LANCZOS)
                        self.image = ImageTk.PhotoImage(image)
                        self.menu_Jeudi_soir = Button(self.fenetre, image = self.image, bd =0, bg = "#ECFFFC", command = lambda: instance.add_recette(jour = ["Jeudi", "soir"]))
                        tooltip = Button(fenetre, text=nom, font = ("",te), bd=0, bg="#ECFFFC", command = lambda : instance.add_recette(jour = ["Jeudi", "soir"]))

                        def enter(event):
                            tooltip.place(x= x2, y=y2)
                            tooltip.lift()
                            
                        def leave(event):
                            tooltip.place_forget()
                        self.menu_Jeudi_soir.bind('<Enter>', enter)
                        self.menu_Jeudi_soir.bind('<Leave>', leave)
                        self.menu_Jeudi_soir.image = self.image 
                        self.menu_Jeudi_soir.place(x= 40 + x *100, y=100 + y *105)
            

        class Vendredi:
            def __init__(self, instance, fenetre, coef = 11, x=1 , y=1, mode = 1):
                if mode == 1:
                    self.fenetre = fenetre
                    chemin_actuel = os.path.abspath(__file__)
                    chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Vendredi.png")
                    image = Image.open(chemin_actuel)
                    image = image.resize((int(1587//coef//1), int(2245//coef//1)), Image.LANCZOS)
                    self.image = ImageTk.PhotoImage(image)
                    self.menu_Vendredi = Button(self.fenetre, image = self.image, activebackground= "magenta", bd =0, command = instance.Menu_Vendredi)
                    self.menu_Vendredi.image = self.image 
                    self.menu_Vendredi.place(x=40 + x *100 + 50*x, y=100 + y *105)
                    self.Recette.recette_midi(self, instance, fenetre=fenetre, coef = 11, x=0.5 , y=2.6, te = "9",x2= 88 + 0.5 *100, y2=100 + 2.6 *105)
                    self.Recette.recette_soir(self, instance, fenetre=fenetre, coef = 11, x=0.5 , y=3.325, te = "9",x2= 88 + 0.5 *100, y2=100 + 3.325 *105)
                elif mode == 2:
                    self.Menu_avec_Vendredi_en_grand( instance, fenetre, coef = coef, x =x , y =y) 

            def Menu_avec_Vendredi_en_grand(self, instance, fenetre, coef = 11, x=1 , y=1):
                self.fenetre = fenetre
                chemin_actuel = os.path.abspath(__file__)
                chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Vendredi.png")
                image = Image.open(chemin_actuel)
                image = image.resize((int(1587//coef//1), int(2245//coef//1)), Image.LANCZOS)
                self.image = ImageTk.PhotoImage(image)
                self.menu_Vendredi = Label(self.fenetre, image = self.image, bd =0)
                self.menu_Vendredi.image = self.image 
                self.menu_Vendredi.place(x= 40 + x *100, y=100 + y *105)
                self.Recette.recette_midi(self, instance, fenetre=fenetre, coef = 6, x=2.3 , y=0.8, te = "20",x2=  120+2.3 *100, y2=100 + 0.8 *105)
                self.Recette.recette_soir(self, instance, fenetre=fenetre, coef = 6, x=2.3 , y=2.6, te = "20",x2=  120+2.3 *100, y2=100 + 2.6 *105)

            class Recette:
                def recette_midi(self, instance, fenetre, coef = 11, x=1 , y=1, te = 1, y2 = 1, x2 = 1):
                        fichier = os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt")
                        dico = {}
                        with open(fichier, "r") as f:
                            contenue = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â")
                            exec(contenue, dico)
                        image = dico['Vendredi_midi_recette'][0]
                        nom = dico["Vendredi_midi_recette"][1]
                        self.fenetre = fenetre
                        chemin = os.path.abspath(__file__).replace("Graphique.py", "icone_recette\\"+image+".png" )
                        image = Image.open(chemin)
                        image = image.resize((int(500//coef//1), int(500//coef//1)), Image.LANCZOS)
                        self.image = ImageTk.PhotoImage(image)
                        self.menu_Vendredi_midi = Button(self.fenetre, image = self.image, bd =0, bg = "#ECFFFC", command = lambda: instance.add_recette(jour = ["Vendredi", "midi"]))
                        tooltip = Button(fenetre, text=nom, font = ("",te), bd=0, bg="#ECFFFC", command = lambda : instance.add_recette(jour = ["Vendredi", "midi"]))

                        def enter(event):
                            tooltip.place(x= x2, y=y2)
                            tooltip.lift()
                            
                        def leave(event):
                            tooltip.place_forget()
                        self.menu_Vendredi_midi.bind('<Enter>', enter)
                        self.menu_Vendredi_midi.bind('<Leave>', leave)
                        self.menu_Vendredi_midi.image = self.image 
                        self.menu_Vendredi_midi.place(x= 40 + x *100, y=100 + y *105)
                
                def recette_soir(self, instance, fenetre, coef = 11, x=1 , y=1, te = 1, y2 = 1, x2 = 1):
                        fichier = os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt")
                        dico = {}
                        with open(fichier, "r") as f:
                            contenue = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â")
                            exec(contenue, dico)
                        image = dico['Vendredi_soir_recette'][0]
                        nom = dico["Vendredi_soir_recette"][1]
                        self.fenetre = fenetre
                        chemin = os.path.abspath(__file__).replace("Graphique.py", "icone_recette\\"+image+".png" )
                        image = Image.open(chemin)
                        image = image.resize((int(500//coef//1), int(500//coef//1)), Image.LANCZOS)
                        self.image = ImageTk.PhotoImage(image)
                        self.menu_Vendredi_soir = Button(self.fenetre, image = self.image, bd =0, bg = "#ECFFFC", command = lambda: instance.add_recette(jour = ["Vendredi", "soir"]))
                        tooltip = Button(fenetre, text=nom, font = ("",te), bd=0, bg="#ECFFFC", command = lambda : instance.add_recette(jour = ["Vendredi", "soir"]))

                        def enter(event):
                            tooltip.place(x= x2, y=y2)
                            tooltip.lift()
                            
                        def leave(event):
                            tooltip.place_forget()
                        self.menu_Vendredi_soir.bind('<Enter>', enter)
                        self.menu_Vendredi_soir.bind('<Leave>', leave)
                        self.menu_Vendredi_soir.image = self.image 
                        self.menu_Vendredi_soir.place(x= 40 + x *100, y=100 + y *105)
            

        class Samedi:
            def __init__(self, instance, fenetre, coef = 11, x=1 , y=1, mode = 1):
                if mode == 1:
                    self.fenetre = fenetre
                    chemin_actuel = os.path.abspath(__file__)
                    chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Samedi.png")
                    image = Image.open(chemin_actuel)
                    image = image.resize((int(1587//coef//1), int(2245//coef//1)), Image.LANCZOS)
                    self.image = ImageTk.PhotoImage(image)
                    self.menu_Samedi = Button(self.fenetre, image = self.image, activebackground= "magenta", bd =0, command = instance.Menu_Samedi)
                    self.menu_Samedi.image = self.image 
                    self.menu_Samedi.place(x=40 + x *100 + 50*x, y=100 + y *105)
                    self.Recette.recette_midi(self, instance, fenetre=fenetre, coef = 11, x=2 , y=2.6, te = "9",x2= 88 + 2 *100, y2=100 + 2.6 *105)
                    self.Recette.recette_soir(self, instance, fenetre=fenetre, coef = 11, x=2 , y=3.325, te = "9",x2= 88 + 2 *100, y2=100 + 3.325 *105)
                elif mode == 2:
                    self.Menu_avec_Samedi_en_grand( instance, fenetre, coef = coef, x =x , y =y) 

            def Menu_avec_Samedi_en_grand(self, instance, fenetre, coef = 11, x=1 , y=1):
                self.fenetre = fenetre
                chemin_actuel = os.path.abspath(__file__)
                chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Samedi.png")
                image = Image.open(chemin_actuel)
                image = image.resize((int(1587//coef//1), int(2245//coef//1)), Image.LANCZOS)
                self.image = ImageTk.PhotoImage(image)
                self.menu_Samedi = Label(self.fenetre, image = self.image, bd =0)
                self.menu_Samedi.image = self.image 
                self.menu_Samedi.place(x= 40 + x *100, y=100 + y *105)
                self.Recette.recette_midi(self, instance, fenetre=fenetre, coef = 6, x=2.3 , y=0.8, te = "20",x2=  120+2.3 *100, y2=100 + 0.8 *105)
                self.Recette.recette_soir(self, instance, fenetre=fenetre, coef = 6, x=2.3 , y=2.6, te = "20",x2=  120+2.3 *100, y2=100 + 2.6 *105)

            class Recette:
                def recette_midi(self, instance, fenetre, coef = 11, x=1 , y=1, te = 1, y2 = 1, x2 = 1):
                        fichier = os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt")
                        dico = {}
                        with open(fichier, "r") as f:
                            contenue = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â")
                            exec(contenue, dico)
                        image = dico['Samedi_midi_recette'][0]
                        nom = dico["Samedi_midi_recette"][1]
                        self.fenetre = fenetre
                        chemin = os.path.abspath(__file__).replace("Graphique.py", "icone_recette\\"+image+".png" )
                        image = Image.open(chemin)
                        image = image.resize((int(500//coef//1), int(500//coef//1)), Image.LANCZOS)
                        self.image = ImageTk.PhotoImage(image)
                        self.menu_Samedi_midi = Button(self.fenetre, image = self.image, bd =0, bg = "#ECFFFC", command = lambda: instance.add_recette(jour = ["Samedi", "midi"]))
                        tooltip = Button(fenetre, text=nom, font = ("",te), bd=0, bg="#ECFFFC", command = lambda : instance.add_recette(jour = ["Samedi", "midi"]))

                        def enter(event):
                            tooltip.place(x= x2, y=y2)
                            tooltip.lift()
                            
                        def leave(event):
                            tooltip.place_forget()
                        self.menu_Samedi_midi.bind('<Enter>', enter)
                        self.menu_Samedi_midi.bind('<Leave>', leave)
                        self.menu_Samedi_midi.image = self.image 
                        self.menu_Samedi_midi.place(x= 40 + x *100, y=100 + y *105)
                
                def recette_soir(self, instance, fenetre, coef = 11, x=1 , y=1, te = 1, y2 = 1, x2 = 1):
                        fichier = os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt")
                        dico = {}
                        with open(fichier, "r") as f:
                            contenue = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â")
                            exec(contenue, dico)
                        image = dico['Samedi_soir_recette'][0]
                        nom = dico["Samedi_soir_recette"][1]
                        self.fenetre = fenetre
                        chemin = os.path.abspath(__file__).replace("Graphique.py", "icone_recette\\"+image+".png" )
                        image = Image.open(chemin)
                        image = image.resize((int(500//coef//1), int(500//coef//1)), Image.LANCZOS)
                        self.image = ImageTk.PhotoImage(image)
                        self.menu_Samedi_soir = Button(self.fenetre, image = self.image, bd =0, bg = "#ECFFFC", command = lambda: instance.add_recette(jour = ["Samedi", "soir"]))
                        tooltip = Button(fenetre, text=nom, font = ("",te), bd=0, bg="#ECFFFC", command = lambda : instance.add_recette(jour = ["Samedi", "soir"]))

                        def enter(event):
                            tooltip.place(x= x2, y=y2)
                            tooltip.lift()
                            
                        def leave(event):
                            tooltip.place_forget()
                        self.menu_Samedi_soir.bind('<Enter>', enter)
                        self.menu_Samedi_soir.bind('<Leave>', leave)
                        self.menu_Samedi_soir.image = self.image 
                        self.menu_Samedi_soir.place(x= 40 + x *100, y=100 + y *105)

        class Dimanche:
            def __init__(self, instance, fenetre, coef = 11, x=1 , y=1, mode = 1):
                if mode == 1:
                    self.fenetre = fenetre
                    chemin_actuel = os.path.abspath(__file__)
                    chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Dimanche.png")
                    image = Image.open(chemin_actuel)
                    image = image.resize((int(1587//coef//1), int(2245//coef//1)), Image.LANCZOS)
                    self.image = ImageTk.PhotoImage(image)
                    self.menu_Dimanche = Button(self.fenetre, image = self.image, activebackground= "magenta", bd =0, command = instance.Menu_Dimanche)
                    self.menu_Dimanche.image = self.image 
                    self.menu_Dimanche.place(x=40 + x *100 + 50*x, y=100 + y *105)
                    self.Recette.recette_midi(self, instance, fenetre=fenetre, coef = 11, x=3.5 , y=2.6, te = "9",x2= 88 + 3.5 *100, y2=100 + 2.6 *105)
                    self.Recette.recette_soir(self, instance, fenetre=fenetre, coef = 11, x=3.5 , y=3.325, te = "9",x2= 88 + 3.5 *100, y2=100 + 3.325 *105)
                elif mode == 2:
                    self.Menu_avec_Dimanche_en_grand( instance, fenetre, coef = coef, x =x , y =y) 

            def Menu_avec_Dimanche_en_grand(self, instance, fenetre, coef = 11, x=1 , y=1):
                self.fenetre = fenetre
                chemin_actuel = os.path.abspath(__file__)
                chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Dimanche.png")
                image = Image.open(chemin_actuel)
                image = image.resize((int(1587//coef//1), int(2245//coef//1)), Image.LANCZOS)
                self.image = ImageTk.PhotoImage(image)
                self.menu_Dimanche = Label(self.fenetre, image = self.image, bd =0)
                self.menu_Dimanche.image = self.image 
                self.menu_Dimanche.place(x= 40 + x *100, y=100 + y *105)
                self.Recette.recette_midi(self, instance, fenetre=fenetre, coef = 6, x=2.3 , y=0.8, te = "20",x2=  120+2.3 *100, y2=100 + 0.8 *105)
                self.Recette.recette_soir(self, instance, fenetre=fenetre, coef = 6, x=2.3 , y=2.6, te = "20",x2=  120+2.3 *100, y2=100 + 2.6 *105)

            class Recette:
                def recette_midi(self, instance, fenetre, coef = 11, x=1 , y=1, te = 1, y2 = 1, x2 = 1):
                        fichier = os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt")
                        dico = {}
                        with open(fichier, "r") as f:
                            contenue = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â")
                            exec(contenue, dico)
                        image = dico['Dimanche_midi_recette'][0]
                        nom = dico["Dimanche_midi_recette"][1]
                        self.fenetre = fenetre
                        chemin = os.path.abspath(__file__).replace("Graphique.py", "icone_recette\\"+image+".png" )
                        image = Image.open(chemin)
                        image = image.resize((int(500//coef//1), int(500//coef//1)), Image.LANCZOS)
                        self.image = ImageTk.PhotoImage(image)
                        self.menu_Dimanche_midi = Button(self.fenetre, image = self.image, bd =0, bg = "#ECFFFC", command = lambda: instance.add_recette(jour = ["Dimanche", "midi"]))
                        tooltip = Button(fenetre, text=nom, font = ("",te), bd=0, bg="#ECFFFC", command = lambda : instance.add_recette(jour = ["Dimanche", "midi"]))

                        def enter(event):
                            tooltip.place(x= x2, y=y2)
                            tooltip.lift()
                            
                        def leave(event):
                            tooltip.place_forget()
                        self.menu_Dimanche_midi.bind('<Enter>', enter)
                        self.menu_Dimanche_midi.bind('<Leave>', leave)
                        self.menu_Dimanche_midi.image = self.image 
                        self.menu_Dimanche_midi.place(x= 40 + x *100, y=100 + y *105)
                
                def recette_soir(self, instance, fenetre, coef = 11, x=1 , y=1, te = 1, y2 = 1, x2 = 1):
                        fichier = os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt")
                        dico = {}
                        with open(fichier, "r") as f:
                            contenue = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â")
                            exec(contenue, dico)
                        image = dico['Dimanche_soir_recette'][0]
                        nom = dico["Dimanche_soir_recette"][1]
                        self.fenetre = fenetre
                        chemin = os.path.abspath(__file__).replace("Graphique.py", "icone_recette\\"+image+".png" )
                        image = Image.open(chemin)
                        image = image.resize((int(500//coef//1), int(500//coef//1)), Image.LANCZOS)
                        self.image = ImageTk.PhotoImage(image)
                        self.menu_Dimanche_soir = Button(self.fenetre, image = self.image, bd =0, bg = "#ECFFFC", command = lambda: instance.add_recette(jour = ["Dimanche", "soir"]))
                        tooltip = Button(fenetre, text=nom, font = ("",te), bd=0, bg="#ECFFFC", command = lambda : instance.add_recette(jour = ["Dimanche", "soir"]))

                        def enter(event):
                            tooltip.place(x= x2, y=y2)
                            tooltip.lift()
                            
                        def leave(event):
                            tooltip.place_forget()
                        self.menu_Dimanche_soir.bind('<Enter>', enter)
                        self.menu_Dimanche_soir.bind('<Leave>', leave)
                        self.menu_Dimanche_soir.image = self.image 
                        self.menu_Dimanche_soir.place(x= 40 + x *100, y=100 + y *105)
        
        class Extra:
            def __init__(self, instance, fenetre, coef = 11, x=1 , y=1, mode = 1):
                if mode == 1:
                    self.fenetre = fenetre
                    chemin_actuel = os.path.abspath(__file__)
                    chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Extra.png")
                    image = Image.open(chemin_actuel)
                    image = image.resize((int(1587//coef//1), int(2245//coef//1)), Image.LANCZOS)
                    self.image = ImageTk.PhotoImage(image)
                    self.menu_Extra = Button(self.fenetre, image = self.image, activebackground= "magenta", bd =0, command = instance.Menu_Extra)
                    self.menu_Extra.image = self.image 
                    self.menu_Extra.place(x=40 + x *100 + 50*x, y=100 + y *105)
                    self.Recette.recette_midi(self, instance, fenetre=fenetre, coef = 11, x=5 , y=2.6, te = "9",x2= 88 + 5 *100, y2=100 + 2.6 *105)
                    self.Recette.recette_soir(self, instance, fenetre=fenetre, coef = 11, x=5 , y=3.325, te = "9",x2= 88 + 5 *100, y2=100 + 3.325 *105)
                elif mode == 2:
                    self.Menu_avec_Extra_en_grand( instance, fenetre, coef = coef, x =x , y =y) 

            def Menu_avec_Extra_en_grand(self, instance, fenetre, coef = 11, x=1 , y=1):
                self.fenetre = fenetre
                chemin_actuel = os.path.abspath(__file__)
                chemin_actuel = chemin_actuel.replace("Graphique.py", "image\\Extra.png")
                image = Image.open(chemin_actuel)
                image = image.resize((int(1587//coef//1), int(2245//coef//1)), Image.LANCZOS)
                self.image = ImageTk.PhotoImage(image)
                self.menu_Extra = Label(self.fenetre, image = self.image, bd =0)
                self.menu_Extra.image = self.image 
                self.menu_Extra.place(x= 40 + x *100, y=100 + y *105)
                self.Recette.recette_midi(self, instance, fenetre=fenetre, coef = 6, x=2.3 , y=0.8, te = "20",x2=  120+2.3 *100, y2=100 + 0.8 *105)
                self.Recette.recette_soir(self, instance, fenetre=fenetre, coef = 6, x=2.3 , y=2.6, te = "20",x2=  120+2.3 *100, y2=100 + 2.6 *105)

            class Recette:
                def recette_midi(self, instance, fenetre, coef = 11, x=1 , y=1, te = 1, y2 = 1, x2 = 1):
                        fichier = os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt")
                        dico = {}
                        with open(fichier, "r") as f:
                            contenue = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â")
                            exec(contenue, dico)
                        image = dico['Extra_midi_recette'][0]
                        nom = dico["Extra_midi_recette"][1]
                        self.fenetre = fenetre
                        chemin = os.path.abspath(__file__).replace("Graphique.py", "icone_recette\\"+image+".png" )
                        image = Image.open(chemin)
                        image = image.resize((int(500//coef//1), int(500//coef//1)), Image.LANCZOS)
                        self.image = ImageTk.PhotoImage(image)
                        self.menu_Extra_midi = Button(self.fenetre, image = self.image, bd =0, bg = "#ECFFFC", command = lambda: instance.add_recette(jour = ["Extra", "midi"]))
                        tooltip = Button(fenetre, text=nom, font = ("",te), bd=0, bg="#ECFFFC", command = lambda : instance.add_recette(jour = ["Extra", "midi"]))

                        def enter(event):
                            tooltip.place(x= x2, y=y2)
                            tooltip.lift()
                            
                        def leave(event):
                            tooltip.place_forget()
                        self.menu_Extra_midi.bind('<Enter>', enter)
                        self.menu_Extra_midi.bind('<Leave>', leave)
                        self.menu_Extra_midi.image = self.image 
                        self.menu_Extra_midi.place(x= 40 + x *100, y=100 + y *105)
                
                def recette_soir(self, instance, fenetre, coef = 11, x=1 , y=1, te = 1, y2 = 1, x2 = 1):
                        fichier = os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt")
                        dico = {}
                        with open(fichier, "r") as f:
                            contenue = f.read().replace("Â°", "°").replace("Ã»", "u").replace("Ã¨", "è").replace("Ã©", "é").replace("â€“", "-").replace("Ãª", "ê").replace("Ã¢", "â").replace("ï¿½", "â")
                            exec(contenue, dico)
                        image = dico['Extra_soir_recette'][0]
                        nom = dico["Extra_soir_recette"][1]
                        self.fenetre = fenetre
                        chemin = os.path.abspath(__file__).replace("Graphique.py", "icone_recette\\"+image+".png" )
                        image = Image.open(chemin)
                        image = image.resize((int(500//coef//1), int(500//coef//1)), Image.LANCZOS)
                        self.image = ImageTk.PhotoImage(image)
                        self.menu_Extra_soir = Button(self.fenetre, image = self.image, bd =0, bg = "#ECFFFC", command = lambda: instance.add_recette(jour = ["Extra", "soir"]))
                        tooltip = Button(fenetre, text=nom, font = ("",te), bd=0, bg="#ECFFFC", command = lambda : instance.add_recette(jour = ["Extra", "soir"]))

                        def enter(event):
                            tooltip.place(x= x2, y=y2)
                            tooltip.lift()
                            
                        def leave(event):
                            tooltip.place_forget()
                        self.menu_Extra_soir.bind('<Enter>', enter)
                        self.menu_Extra_soir.bind('<Leave>', leave)
                        self.menu_Extra_soir.image = self.image 
                        self.menu_Extra_soir.place(x= 40 + x *100, y=100 + y *105)
    




    class menu_recette:
        def __init__(self, instance,fenetre, coef = 11, x=1 , y=1, image = "", nom = "", jour = ["", ""]):
            image_heritage = image
            self.sauvegarde_bouton = []
            self.fenetre = fenetre
            chemin = os.path.abspath(__file__).replace("Graphique.py", "icone_recette\\"+image+".png" )
            image = Image.open(chemin)
            image = image.resize((int(125//coef//1), int(125//coef//1)), Image.LANCZOS)
            self.image = ImageTk.PhotoImage(image)
            self.menu_image = Button(self.fenetre, image = self.image, bd =1, bg = "black", command = lambda : self.commande(jour, instance,image_heritage, nom))
            self.menu_image.image = self.image 
            self.menu_image.place(x=x, y=y)
            meni_nom = Label(self.fenetre, text = nom, bg = "#D1FFF7", font = ("", "8"))
            meni_nom.place(x=x, y=y+67)
            self.sauvegarde_bouton.append(self.menu_image)
            instance.memoire.append([self.menu_image, meni_nom])
        
        def commande(self, jour,instance, image, nom_de_la_recette):
            
            match jour[0]:
                case "Lundi":
                    match jour[1]:
                        case "midi":
                            try:
                                self.menu_image.config(command = self.changement.Lundi.midi(self, instance, nouvelle_image = image, nom_de_la_recette  = nom_de_la_recette))
                            except:
                                pass
                        case "soir":
                            try:
                                self.menu_image.config(command = self.changement.Lundi.soir(self, instance, nouvelle_image = image, nom_de_la_recette  = nom_de_la_recette))
                            except:
                                pass

                case "Mardi":
                    match jour[1]:
                        case "midi":
                            try:
                                self.menu_image.config(command = self.changement.Mardi.midi(self, instance, nouvelle_image = image, nom_de_la_recette  = nom_de_la_recette))
                            except:
                                pass
                        
                        case "soir":
                            try:
                                self.menu_image.config(command = self.changement.Mardi.soir(self, instance, nouvelle_image = image, nom_de_la_recette  = nom_de_la_recette))
                            except:
                                pass
                            
                case "Mercredi":
                    match jour[1]:
                        case "midi":
                            try:
                                self.menu_image.config(command = self.changement.Mercredi.midi(self, instance, nouvelle_image = image, nom_de_la_recette  = nom_de_la_recette))
                            except:
                                pass
                        
                        case "soir":
                            try:
                                self.menu_image.config(command = self.changement.Mercredi.soir(self, instance, nouvelle_image = image, nom_de_la_recette  = nom_de_la_recette))
                            except:
                                pass
                            
                case "Jeudi":
                    match jour[1]:
                        case "midi":
                            try:
                                self.menu_image.config(command = self.changement.Jeudi.midi(self, instance, nouvelle_image = image, nom_de_la_recette  = nom_de_la_recette))
                            except:
                                pass
                        
                        case "soir":
                            try:
                                self.menu_image.config(command = self.changement.Jeudi.soir(self, instance, nouvelle_image = image, nom_de_la_recette  = nom_de_la_recette))
                            except:
                                pass
                            
                case "Vendredi":
                    match jour[1]:
                        case "midi":
                            try:
                                self.menu_image.config(command = self.changement.Vendredi.midi(self, instance, nouvelle_image = image, nom_de_la_recette  = nom_de_la_recette))
                            except:
                                pass
                        
                        case "soir":
                            try:
                                self.menu_image.config(command = self.changement.Vendredi.soir(self, instance, nouvelle_image = image, nom_de_la_recette  = nom_de_la_recette))
                            except:
                                pass

                case "Samedi":
                    match jour[1]:
                        case "midi":
                            try:
                                self.menu_image.config(command = self.changement.Samedi.midi(self, instance, nouvelle_image = image, nom_de_la_recette  = nom_de_la_recette))
                            except:
                                pass
                        
                        case "soir":
                            try:
                                self.menu_image.config(command = self.changement.Samedi.soir(self, instance, nouvelle_image = image, nom_de_la_recette  = nom_de_la_recette))
                            except:
                                pass
                            
                case "Dimanche":
                    match jour[1]:
                        case "midi":
                            try:
                                self.menu_image.config(command = self.changement.Dimanche.midi(self, instance, nouvelle_image = image, nom_de_la_recette  = nom_de_la_recette))
                            except:
                                pass
                        
                        case "soir":
                            try:
                                self.menu_image.config(command = self.changement.Dimanche.soir(self, instance, nouvelle_image = image, nom_de_la_recette  = nom_de_la_recette))
                            except:
                                pass
                            
                case "Extra":
                    match jour[1]:
                        case "midi":
                            try:
                                self.menu_image.config(command = self.changement.Extra.midi(self, instance, nouvelle_image = image, nom_de_la_recette  = nom_de_la_recette))
                            except:
                                pass
                        
                        case "soir":
                            try:
                                self.menu_image.config(command = self.changement.Extra.soir(self, instance, nouvelle_image = image, nom_de_la_recette  = nom_de_la_recette))
                            except:
                                pass
                    
        class changement:
            class Lundi:            
                def midi(self, instance, nouvelle_image = "a selectionner",  nom_de_la_recette = "Rien" ):
                    dico = {}
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "r") as f:
                        contenu = f.read()
                        exec(contenu, dico)
                    image = dico['Lundi_midi_recette'][0] 
                    nom = dico['Lundi_midi_recette'][1] 
                    contenu = contenu.replace('Lundi_midi_recette = ["'+image+'", "'+nom.replace("\n", "\\n")+'"]', 'Lundi_midi_recette = ["'+nouvelle_image+'", "'+nom_de_la_recette.replace("\n", "\\n")+'"]')
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "w") as f:
                        f.write(contenu)
                    instance.add_recette(jour = ["Lundi", "midi"])
                
                def soir(self, instance, nouvelle_image = "a selectionner",  nom_de_la_recette = "Rien" ):
                    dico = {}
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "r") as f:
                        contenu = f.read()
                        exec(contenu, dico)
                    image = dico['Lundi_soir_recette'][0] 
                    nom = dico['Lundi_soir_recette'][1] 
                    contenu = contenu.replace('Lundi_soir_recette = ["'+image+'", "'+nom.replace("\n", "\\n")+'"]', 'Lundi_soir_recette = ["'+nouvelle_image+'", "'+nom_de_la_recette.replace("\n", "\\n")+'"]')
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "w") as f:
                        f.write(contenu)
                    instance.add_recette(jour = ["Lundi", "soir"])
            
            class Mardi:            
                def midi(self, instance, nouvelle_image = "a selectionner",  nom_de_la_recette = "Rien" ):
                    dico = {}
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "r") as f:
                        contenu = f.read()
                        exec(contenu, dico)
                    image = dico['Mardi_midi_recette'][0] 
                    nom = dico['Mardi_midi_recette'][1] 
                    contenu = contenu.replace('Mardi_midi_recette = ["'+image+'", "'+nom.replace("\n", "\\n")+'"]', 'Mardi_midi_recette = ["'+nouvelle_image+'", "'+nom_de_la_recette.replace("\n", "\\n")+'"]')
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "w") as f:
                        f.write(contenu)
                    instance.add_recette(jour = ["Mardi", "midi"])
                
                def soir(self, instance, nouvelle_image = "a selectionner",  nom_de_la_recette = "Rien" ):
                    dico = {}
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "r") as f:
                        contenu = f.read()
                        exec(contenu, dico)
                    image = dico['Mardi_soir_recette'][0] 
                    nom = dico['Mardi_soir_recette'][1] 
                    contenu = contenu.replace('Mardi_soir_recette = ["'+image+'", "'+nom.replace("\n", "\\n")+'"]', 'Mardi_soir_recette = ["'+nouvelle_image+'", "'+nom_de_la_recette.replace("\n", "\\n")+'"]')
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "w") as f:
                        f.write(contenu)
                    instance.add_recette(jour = ["Mardi", "soir"])
                    
            class Mercredi:            
                def midi(self, instance, nouvelle_image = "a selectionner",  nom_de_la_recette = "Rien" ):
                    dico = {}
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "r") as f:
                        contenu = f.read()
                        exec(contenu, dico)
                    image = dico['Mercredi_midi_recette'][0] 
                    nom = dico['Mercredi_midi_recette'][1] 
                    contenu = contenu.replace('Mercredi_midi_recette = ["'+image+'", "'+nom.replace("\n", "\\n")+'"]', 'Mercredi_midi_recette = ["'+nouvelle_image+'", "'+nom_de_la_recette.replace("\n", "\\n")+'"]')
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "w") as f:
                        f.write(contenu)
                    instance.add_recette(jour = ["Mercredi", "midi"])
                
                def soir(self, instance, nouvelle_image = "a selectionner",  nom_de_la_recette = "Rien" ):
                    dico = {}
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "r") as f:
                        contenu = f.read()
                        exec(contenu, dico)
                    image = dico['Mercredi_soir_recette'][0] 
                    nom = dico['Mercredi_soir_recette'][1] 
                    contenu = contenu.replace('Mercredi_soir_recette = ["'+image+'", "'+nom.replace("\n", "\\n")+'"]', 'Mercredi_soir_recette = ["'+nouvelle_image+'", "'+nom_de_la_recette.replace("\n", "\\n")+'"]')
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "w") as f:
                        f.write(contenu)
                    instance.add_recette(jour = ["Mercredi", "soir"])
                    
            class Jeudi:            
                def midi(self, instance, nouvelle_image = "a selectionner",  nom_de_la_recette = "Rien" ):
                    dico = {}
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "r") as f:
                        contenu = f.read()
                        exec(contenu, dico)
                    image = dico['Jeudi_midi_recette'][0] 
                    nom = dico['Jeudi_midi_recette'][1] 
                    contenu = contenu.replace('Jeudi_midi_recette = ["'+image+'", "'+nom.replace("\n", "\\n")+'"]', 'Jeudi_midi_recette = ["'+nouvelle_image+'", "'+nom_de_la_recette.replace("\n", "\\n")+'"]')
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "w") as f:
                        f.write(contenu)
                    instance.add_recette(jour = ["Jeudi", "midi"])
                
                def soir(self, instance, nouvelle_image = "a selectionner",  nom_de_la_recette = "Rien" ):
                    dico = {}
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "r") as f:
                        contenu = f.read()
                        exec(contenu, dico)
                    image = dico['Jeudi_soir_recette'][0] 
                    nom = dico['Jeudi_soir_recette'][1] 
                    contenu = contenu.replace('Jeudi_soir_recette = ["'+image+'", "'+nom.replace("\n", "\\n")+'"]', 'Jeudi_soir_recette = ["'+nouvelle_image+'", "'+nom_de_la_recette.replace("\n", "\\n")+'"]')
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "w") as f:
                        f.write(contenu)
                    instance.add_recette(jour = ["Jeudi", "soir"])
            
            
            class Vendredi:            
                def midi(self, instance, nouvelle_image = "a selectionner",  nom_de_la_recette = "Rien" ):
                    dico = {}
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "r") as f:
                        contenu = f.read()
                        exec(contenu, dico)
                    image = dico['Vendredi_midi_recette'][0] 
                    nom = dico['Vendredi_midi_recette'][1] 
                    contenu = contenu.replace('Vendredi_midi_recette = ["'+image+'", "'+nom.replace("\n", "\\n")+'"]', 'Vendredi_midi_recette = ["'+nouvelle_image+'", "'+nom_de_la_recette.replace("\n", "\\n")+'"]')
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "w") as f:
                        f.write(contenu)
                    instance.add_recette(jour = ["Vendredi", "midi"])
                
                def soir(self, instance, nouvelle_image = "a selectionner",  nom_de_la_recette = "Rien" ):
                    dico = {}
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "r") as f:
                        contenu = f.read()
                        exec(contenu, dico)
                    image = dico['Vendredi_soir_recette'][0] 
                    nom = dico['Vendredi_soir_recette'][1] 
                    contenu = contenu.replace('Vendredi_soir_recette = ["'+image+'", "'+nom.replace("\n", "\\n")+'"]', 'Vendredi_soir_recette = ["'+nouvelle_image+'", "'+nom_de_la_recette.replace("\n", "\\n")+'"]')
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "w") as f:
                        f.write(contenu)
                    instance.add_recette(jour = ["Vendredi", "soir"])
            
            class Samedi:            
                def midi(self, instance, nouvelle_image = "a selectionner",  nom_de_la_recette = "Rien" ):
                    dico = {}
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "r") as f:
                        contenu = f.read()
                        exec(contenu, dico)
                    image = dico['Samedi_midi_recette'][0] 
                    nom = dico['Samedi_midi_recette'][1] 
                    contenu = contenu.replace('Samedi_midi_recette = ["'+image+'", "'+nom.replace("\n", "\\n")+'"]', 'Samedi_midi_recette = ["'+nouvelle_image+'", "'+nom_de_la_recette.replace("\n", "\\n")+'"]')
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "w") as f:
                        f.write(contenu)
                    instance.add_recette(jour = ["Samedi", "midi"])
                
                def soir(self, instance, nouvelle_image = "a selectionner",  nom_de_la_recette = "Rien" ):
                    dico = {}
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "r") as f:
                        contenu = f.read()
                        exec(contenu, dico)
                    image = dico['Samedi_soir_recette'][0] 
                    nom = dico['Samedi_soir_recette'][1] 
                    contenu = contenu.replace('Samedi_soir_recette = ["'+image+'", "'+nom.replace("\n", "\\n")+'"]', 'Samedi_soir_recette = ["'+nouvelle_image+'", "'+nom_de_la_recette.replace("\n", "\\n")+'"]')
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "w") as f:
                        f.write(contenu)
                    instance.add_recette(jour = ["Samedi", "soir"])
            
            class Dimanche:            
                def midi(self, instance, nouvelle_image = "a selectionner",  nom_de_la_recette = "Rien" ):
                    dico = {}
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "r") as f:
                        contenu = f.read()
                        exec(contenu, dico)
                    image = dico['Dimanche_midi_recette'][0] 
                    nom = dico['Dimanche_midi_recette'][1] 
                    contenu = contenu.replace('Dimanche_midi_recette = ["'+image+'", "'+nom.replace("\n", "\\n")+'"]', 'Dimanche_midi_recette = ["'+nouvelle_image+'", "'+nom_de_la_recette.replace("\n", "\\n")+'"]')
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "w") as f:
                        f.write(contenu)
                    instance.add_recette(jour = ["Dimanche", "midi"])
                
                def soir(self, instance, nouvelle_image = "a selectionner",  nom_de_la_recette = "Rien" ):
                    dico = {}
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "r") as f:
                        contenu = f.read()
                        exec(contenu, dico)
                    image = dico['Dimanche_soir_recette'][0] 
                    nom = dico['Dimanche_soir_recette'][1] 
                    contenu = contenu.replace('Dimanche_soir_recette = ["'+image+'", "'+nom.replace("\n", "\\n")+'"]', 'Dimanche_soir_recette = ["'+nouvelle_image+'", "'+nom_de_la_recette.replace("\n", "\\n")+'"]')
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "w") as f:
                        f.write(contenu)
                    instance.add_recette(jour = ["Dimanche", "soir"])
            
            class Extra:            
                def midi(self, instance, nouvelle_image = "a selectionner",  nom_de_la_recette = "Rien" ):
                    dico = {}
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "r") as f:
                        contenu = f.read()
                        exec(contenu, dico)
                    image = dico['Extra_midi_recette'][0] 
                    nom = dico['Extra_midi_recette'][1] 
                    contenu = contenu.replace('Extra_midi_recette = ["'+image+'", "'+nom.replace("\n", "\\n")+'"]', 'Extra_midi_recette = ["'+nouvelle_image+'", "'+nom_de_la_recette.replace("\n", "\\n")+'"]')
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "w") as f:
                        f.write(contenu)
                    instance.add_recette(jour = ["Extra", "midi"])
                
                def soir(self, instance, nouvelle_image = "a selectionner",  nom_de_la_recette = "Rien" ):
                    dico = {}
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "r") as f:
                        contenu = f.read()
                        exec(contenu, dico)
                    image = dico['Extra_soir_recette'][0] 
                    nom = dico['Extra_soir_recette'][1] 
                    contenu = contenu.replace('Extra_soir_recette = ["'+image+'", "'+nom.replace("\n", "\\n")+'"]', 'Extra_soir_recette = ["'+nouvelle_image+'", "'+nom_de_la_recette.replace("\n", "\\n")+'"]')
                    with open(os.path.abspath(__file__).replace("Graphique.py", "recette_actuel.txt"), "w") as f:
                        f.write(contenu)
                    instance.add_recette(jour = ["Extra", "soir"])
            
            
                    
