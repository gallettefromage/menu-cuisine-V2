from tkinter import *
import os
from PIL import ImageTk, Image
import Graphique
from tkinter import ttk
import Trier_recette, menu_recette
class init: 
    def __init__(self, fenetre, instance_code_prin):
        selection = Toplevel(fenetre, bg = "light blue")
        selection.geometry("480x480")
        selection.grab_set()

        class selection_du_type:
                        
             def __init__(self, selection,x,y, instance, instance_code_prin):
                            
                            instance.endroitmenu2 = Label(selection)
                            instance.endroitmenu2.place(x= x+0, y = y+0)


                            instance.btn_selection_du_type2 = Menubutton(instance.endroitmenu2, text = "Type : a selectionner", bd = 0, relief = "raised", font = ('', "9"), activebackground= "light blue")
                            instance.btn_selection_du_type2.grid(column= 0, row=0, padx = 0, pady= 0)
                            
                            
                            instance.menu_type2 = Menu(instance.btn_selection_du_type2, tearoff=0)
                            instance.btn_selection_du_type2.config(menu = instance.menu_type2)


                            instance.Sucré2 = Menu(instance.menu_type2, tearoff=0)

                            def gâteau():
                                instance.btn_selection_du_type2.config(text = "Type : Gâteau (Sucré)")

                            instance.Sucré2.add_cascade(label = "Gâteau", command = gâteau)
                            instance.Sucré2.add_separator()

                            def Biscuit():
                                instance.btn_selection_du_type2.config(text = "Type : Biscuit (Sucré)")

                            instance.Sucré2.add_command(label = "Biscuit", command = Biscuit)
                            instance.Sucré2.add_separator()

                            def Fête():
                                instance.btn_selection_du_type2.config(text = "Type : Fête (Sucré)")

                            instance.Sucré2.add_command(label = "Fête", command = Fête)
                            instance.menu_type2.add_cascade(menu=instance.Sucré2, label = "Sucré")
                            instance.menu_type2.add_separator()



                            instance.Salé2 = Menu(instance.menu_type2, tearoff=0)
                            instance.végé2 = Menu(instance.Salé2, tearoff=0)
                        
                            def végé_riz():
                                instance.btn_selection_du_type2.config(text = "Type : Riz (Salé - Végétarien)")

                            instance.végé2.add_command(label = "riz", command= végé_riz)
                            instance.végé2.add_separator()

                            def végé_pâte():
                                instance.btn_selection_du_type2.config(text = "Type : Pâte (Salé - Végétarien)")

                            instance.végé2.add_command(label = "pâte", command = végé_pâte)
                            instance.végé2.add_separator()

                            def végé_farine():
                                instance.btn_selection_du_type2.config(text = "Type : Farine (Salé - Végétarien)")

                            instance.végé2.add_command(label = "Farine", command = végé_farine)
                            instance.végé2.add_separator()

                            def végé_pomme_de_terre():
                                instance.btn_selection_du_type2.config(text = "Type : Pomme_de_terre (Salé - Végétarien)")

                            instance.végé2.add_command(label = "Pomme de terre", command = végé_pomme_de_terre)
                            instance.végé2.add_separator()
                            
                            def végé_pain():
                                instance.btn_selection_du_type2.config(text = "Type : Pain (Salé - Végétarien)")

                            instance.végé2.add_command(label = "Pain", command = végé_pain)
                            instance.Salé2.add_cascade(menu = instance.végé2, label = "Végétarien")
                            instance.Salé2.add_separator()




                            instance.nonvégé2 = Menu(instance.Salé2, tearoff=0)

                            def viande():
                                instance.btn_selection_du_type2.config(text = "Type : Viande (Salé - non-végétarien)")

                            instance.nonvégé2.add_command(label = "Viande", command= viande)
                            instance.nonvégé2.add_separator()

                            def riz():
                                instance.btn_selection_du_type2.config(text = "Type : Riz (Salé - non-végétarien)")

                            instance.nonvégé2.add_command(label = "riz", command = riz)
                            instance.nonvégé2.add_separator()

                            def pâte():
                                instance.btn_selection_du_type2.config(text = "Type : Pâte (Salé - non-végétarien)")

                            instance.nonvégé2.add_command(label = "pâte", command = pâte)
                            instance.nonvégé2.add_separator()
                            
                            def farine():
                                instance.btn_selection_du_type2.config(text = "Type : Farine (Salé - non-végétarien)")

                            instance.nonvégé2.add_command(label = "Farine", command = farine)
                            instance.nonvégé2.add_separator()

                            def pomme_de_terre():
                                instance.btn_selection_du_type2.config(text = "Type : Pomme_de_terre (Salé - non-végétarien)")

                            instance.nonvégé2.add_command(label = "Pomme de terre", command = pomme_de_terre)
                            instance.nonvégé2.add_separator()
                            
                            def pain():
                                instance.btn_selection_du_type2.config(text = "Type : Pain (Salé - non-végétarien)")

                            instance.nonvégé2.add_command(label = "Pain", command = pain)

                            instance.Salé2.add_cascade(menu = instance.nonvégé2, label = "non-végétarien")


                            instance.menu_type2.add_cascade(menu=instance.Salé2, label = "Salé")
                            instance.endroitmenu = ""
                            instance.menu_type2.add_separator()
                            def végé():
                                instance.btn_selection_du_type2.config(text = "Type : Végétarien")
                            instance.menu_type2.add_command(label = "Végétarien", command = végé)
                                
                            def nonvégé():
                                instance.btn_selection_du_type2.config(text = "Type : non-végétarien")
                            instance.menu_type2.add_command(label = "non-végétarien", command = nonvégé)
                                
                            def salé():
                                instance.btn_selection_du_type2.config(text = "Type : Salé")
                            instance.menu_type2.add_command(label = "Salé", command = salé)
                                    
                            def Sucré():
                              instance.btn_selection_du_type2.config(text = "Type : Sucré")
                            instance.menu_type2.add_command(label = "Sucré", command = Sucré)
                            class add_type:
                                def __init__(self, x,y,instance):
                                    instance.endroitmenu = Label(selection)
                                    instance.endroitmenu.place(x= x+200, y = y+0)


                                    instance.btn_selection_du_type = Menubutton(instance.endroitmenu, text = "Type : a selectionner", bd = 0, relief = "raised", font = ('', "9"), activebackground= "light blue")
                                    instance.btn_selection_du_type.grid(column= 0, row=0, padx = 0, pady= 0)
                                    
                                    
                                    instance.menu_type = Menu(instance.btn_selection_du_type, tearoff=0)
                                    instance.btn_selection_du_type.config(menu = instance.menu_type)


                                    instance.Sucré = Menu(instance.menu_type, tearoff=0)

                                    def gâteau():
                                        instance.btn_selection_du_type.config(text = "Type : Gâteau")

                                    instance.Sucré.add_cascade(label = "Gâteau", command = gâteau)
                                    instance.Sucré.add_separator()

                                    def Biscuit():
                                        instance.btn_selection_du_type.config(text = "Type : Biscuit")

                                    instance.Sucré.add_command(label = "Biscuit", command = Biscuit)
                                    instance.Sucré.add_separator()

                                    def Fête():
                                        instance.btn_selection_du_type.config(text = "Type : Fête")

                                    instance.Sucré.add_command(label = "Fête", command = Fête)
                                    instance.menu_type.add_cascade(menu=instance.Sucré, label = "Sucré")
                                    instance.menu_type.add_separator()



                                    instance.Salé = Menu(instance.menu_type, tearoff=0)
                                    instance.végé = Menu(instance.Salé, tearoff=0)
                                
                                    def végé_riz():
                                        instance.btn_selection_du_type.config(text = "Type : Riz")

                                    instance.végé.add_command(label = "riz", command= végé_riz)
                                    instance.végé.add_separator()

                                    def végé_pâte():
                                        instance.btn_selection_du_type.config(text = "Type : Pâte")

                                    instance.végé.add_command(label = "pâte", command = végé_pâte)
                                    instance.végé.add_separator()

                                    def végé_farine():
                                        instance.btn_selection_du_type.config(text = "Type : Farine")

                                    instance.végé.add_command(label = "Farine", command = végé_farine)
                                    instance.végé.add_separator()

                                    def végé_pomme_de_terre():
                                        instance.btn_selection_du_type.config(text = "Type : Pomme_de_terre")

                                    instance.végé.add_command(label = "Pomme de terre", command = végé_pomme_de_terre)
                                    instance.végé.add_separator()
                                    
                                    def végé_pain():
                                        instance.btn_selection_du_type.config(text = "Type : Pain")

                                    instance.végé.add_command(label = "Pain", command = végé_pain)
                                    instance.Salé.add_cascade(menu = instance.végé, label = "végétarien")
                                    instance.Salé.add_separator()




                                    instance.nonvégé = Menu(instance.Salé, tearoff=0)

                                    def viande():
                                        instance.btn_selection_du_type.config(text = "Type : Viande")

                                    instance.nonvégé.add_command(label = "Viande", command= viande)
                                    instance.nonvégé.add_separator()

                                    def riz():
                                        instance.btn_selection_du_type.config(text = "Type : Riz")

                                    instance.nonvégé.add_command(label = "riz", command = riz)
                                    instance.nonvégé.add_separator()

                                    def pâte():
                                        instance.btn_selection_du_type.config(text = "Type : Pâte")

                                    instance.nonvégé.add_command(label = "pâte", command = pâte)
                                    instance.nonvégé.add_separator()
                                    
                                    def farine():
                                        instance.btn_selection_du_type.config(text = "Type : Farine")

                                    instance.nonvégé.add_command(label = "Farine", command = farine)
                                    instance.nonvégé.add_separator()

                                    def pomme_de_terre():
                                        instance.btn_selection_du_type.config(text = "Type : Pomme_de_terre")

                                    instance.nonvégé.add_command(label = "Pomme de terre", command = pomme_de_terre)
                                    instance.nonvégé.add_separator()
                                    
                                    def pain():
                                        instance.btn_selection_du_type.config(text = "Type : Pain")

                                    instance.nonvégé.add_command(label = "Pain", command = pain)

                                    instance.Salé.add_cascade(menu = instance.nonvégé, label = "non-végétarien")


                                    instance.menu_type.add_cascade(menu=instance.Salé, label = "Salé")
                                    instance.menu_type.add_separator()
                                    def végé():
                                        instance.btn_selection_du_type.config(text = "Type : végétarien")
                                    instance.menu_type.add_command(label = "végétarien", command = végé)
                                    
                                    def nonvégé():
                                        instance.btn_selection_du_type.config(text = "Type : non-végétarien")
                                    instance.menu_type.add_command(label = "non-végétarien", command = nonvégé)
                                    
                                    def salé():
                                        instance.btn_selection_du_type.config(text = "Type : Salé")
                                    instance.menu_type.add_command(label = "Salé", command = salé)
                                    
                                    def Sucré():
                                        instance.btn_selection_du_type.config(text = "Type : Sucré")
                                    instance.menu_type.add_command(label = "non-végétarien", command = Sucré)
                                    bouton_plus.destroy()
                            bouton_plus = Button(selection, text = " + ", font =("", "15"), activebackground= "light blue", bd = 2, relief= "raised", command= lambda : add_type(x,y,instance))
                            bouton_plus.place(x=x+200, y=y+0)
                            def valider_type(instance):
                                Valider(instance,instance_code_prin)
                            instance.suivante = Button(selection, text = '→', font = ("Comic Sans MS", "40"), bd =0, bg = "light blue", activebackground= "blue", command = lambda : valider_type(instance))
                            instance.suivante.place(x=x+280, y=y+350)

        class Valider:
            def __init__(self, instance, instance_code_prin):
                instance.data = instance.btn_selection_du_type2.cget("text").replace("Type : ", "").replace(" (", " ").replace(" - ", " ").replace(")", "").split(" ")
                instance.endroitmenu2.destroy()
                if not instance.endroitmenu == "" :
                    typerecette = instance.btn_selection_du_type.cget("text").replace("Type : ", "").replace(" (", " ").replace(" - ", " ").replace(")", "").split(" ")
                    for i in range(len(typerecette)):
                        instance.data.append(typerecette[i])
                    instance.endroitmenu.destroy() 
                for widget in fenetre.winfo_children():
                     if isinstance(widget, Button):
                            largeur = widget.winfo_width()
                            if largeur == 66:
                                widget.destroy()
                            
                     if isinstance(widget, Label):
                            taille = widget.cget("font")
                            if taille.replace("{"+"} ","" ) == "8":
                                widget.destroy()
                selection.destroy()
                instance_code_prin.btn_arriere.destroy()
                instance_code_prin.btn_suivant.destroy()
                menu_recette.init.affichage_de_recette_précise(instance, instance.data,instance_code_prin)


        selection_du_type(selection,0,0 , self,instance_code_prin)