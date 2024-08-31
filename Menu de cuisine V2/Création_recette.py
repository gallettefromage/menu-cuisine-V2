from tkinter import *
import os
from PIL import ImageTk, Image
import Graphique
from tkinter import ttk
import Création_recette
class init: 
    def __init__(self, fenetre):
                    self.compteur = 0
                    self.bouton = [[],[],[]]
                    selection = Toplevel(fenetre, bg = "light blue")
                    selection.geometry("480x480")
                    selection.grab_set()
                    self.data = []
                    class selection_du_type:
                        
                        def __init__(self, selection,x,y, instance):
                            instance.position = Label(selection, text = "3/4", font = ("", "30"), bg = "light blue")
                            x_position_indiacateur = 170
                            y_position_indiacateur = 381
                            instance.position.place(x=x+x_position_indiacateur+40, y=y+y_position_indiacateur +15)
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
                            instance.Salé2.add_cascade(menu = instance.végé2, label = "végétarien")
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

                                    bouton_plus.destroy()
                            def suivant(x,y, instance):
                                instance.data.append(instance.btn_selection_du_type2.cget("text").replace("Type : ", "").replace(" (", " ").replace(" - ", " ").replace(")", "").split(" "))
                                instance.endroitmenu2.destroy()
                                if not instance.endroitmenu == "" :
                                    typerecette = instance.btn_selection_du_type.cget("text").replace("Type : ", "").replace(" (", " ").replace(" - ", " ").replace(")", "").split(" ")
                                    for i in range(len(typerecette)):
                                        instance.data[2].append(typerecette[i])
                                    instance.endroitmenu.destroy() 
                                else:
                                    bouton_plus.destroy()
                                    instance.endroitmenu = False
                                instance.selection = commentaire(selection,x,y, instance)

                            instance.suivant = Button(selection, text = '→', font = ("Comic Sans MS", "40"), bd =0, bg = "light blue", activebackground= "blue", command = lambda : suivant(x,y, instance))
                            instance.suivant.place(x=x+280, y=y+350)
                            bouton_plus = Button(selection, text = " + ", font =("", "15"), activebackground= "light blue", bd = 2, relief= "raised", command= lambda : add_type(x,y,instance))
                            bouton_plus.place(x=x+200, y=y+0)


                    class nom_de_la_recette:

                        def __init__(self, selection,x,y, instance):
                            instance.texte = Text(selection, height = 3, width= 12, fg = "light grey", font = ("", "40"), bg = "beige")
                            instance.texte.place(x=x+75, y=y+100)
                            instance.texte.tag_configure("center", justify='center')
                            instance.texte.insert(END, "Donnez le\nnom de votre\nrecette ?",'center')
                            instance.compteur = 1
                            def btn_return(event):
                                instance.compteur +=1
                                instance.texte.config(height = instance.compteur)
                                if instance.compteur == 4:
                                    instance.texte.unbind('<Return>')
                            def centrer_texte(event):
                                instance.texte.tag_add("center", "1.0", "end")
                            def delete_texte(event):
                                instance.texte.delete('1.0', END)
                                instance.texte.config(width= 12, fg = "black", height = instance.compteur)
                                instance.texte.unbind("<Button-1>")
                                instance.texte.bind('<Return>', btn_return)
                            instance.texte.bind("<Button-1>", delete_texte)
                            instance.texte.bind("<KeyRelease>", centrer_texte)
                            
                            def suivant(x,y, instance):
                                instance.data.append(instance.texte.get("1.0", "end-1c"))

                                instance.texte.destroy()
                                instance.selection = ingrédient(selection,x,y, instance)
                            instance.suivant = Button(selection, text = '→', font = ("Comic Sans MS", "40"), bd =0, bg = "light blue", activebackground= "blue", command = lambda : suivant(x,y, instance))
                            instance.suivant.place(x=x+280, y=y+350)

                            instance.position = Label(selection, text = "1/4", font = ("", "30"), bg = "light blue")

                            x_position_indiacateur = 170
                            y_position_indiacateur = 381
                            instance.position.place(x=x+x_position_indiacateur+40, y=y+y_position_indiacateur +15)
                    nom_de_la_recette(selection,0,0, self)



                    
                    class commentaire:
                        def __init__(self, selection, x, y, instance):
                            instance.texte = Text(selection, height = 6, width= 24, fg = "light grey", font = ("", "20"), bg = "beige")
                            instance.texte.place(x=x+75, y=y+100)
                            instance.texte.tag_configure("center", justify='center')
                            instance.texte.insert(END, "Donnez un\ncommentaire ?\n(optionel)",'center')
                            instance.compteur = 1
                            def btn_return(event):
                                instance.compteur +=1
                                instance.texte.config(height = instance.compteur)
                                if instance.compteur == 4:
                                    instance.texte.unbind('<Return>')
                            def centrer_texte(event):
                                instance.texte.tag_add("center", "1.0", "end")
                            def delete_texte(event):
                                instance.texte.delete('1.0', END)
                                instance.texte.config(width= 24, fg = "black", height = instance.compteur)
                                instance.texte.unbind("<Button-1>")
                                instance.texte.bind('<Return>', btn_return)
                            instance.texte.bind("<Button-1>", delete_texte)
                            instance.texte.bind("<KeyRelease>", centrer_texte)
                            
                            def suivant(x,y, instance):
                                instance.data.append(instance.texte.get("1.0", "end-1c"))
                                instance.texte.destroy()
                                instance.selection = valider(selection,x,y, instance)
                            instance.suivant = Button(selection, text = '→', font = ("Comic Sans MS", "40"), bd =0, bg = "light blue", activebackground= "blue", command = lambda : suivant(x,y, instance))
                            instance.suivant.place(x=x+280, y=y+350)

                            instance.position = Label(selection, text = "4/4", font = ("", "30"), bg = "light blue")

                            x_position_indiacateur = 170
                            y_position_indiacateur = 381
                            instance.position.place(x=x+x_position_indiacateur+40, y=y+y_position_indiacateur +15)
                    

                    class ingrédient:
                        def __init__(self, selection, x, y,instance ):
                            instance.position.config(text = "2/4" )
                            def add_infrédient(x,y,a):
                                quantité = Text(selection, height=1, width= 4)
                                quantité.place(x = x+175, y=y+40+30*a.compteur)
                                a.bouton[0].append(quantité)
                                
                                instance.endroitmenu2 = Label(selection)
                                instance.endroitmenu2.place(x = x+215, y=y+40+30*a.compteur)




                                instance.unité = Menubutton(instance.endroitmenu2, text = "g", bd = 0, relief = "raised", font = ('', "8"), activebackground= "light blue")
                                instance.unité.grid(column= 0, row=0, padx = 0, pady= 0)
                                
                                
                                instance.unité_selec = Menu(instance.unité, tearoff=0)
                                instance.unité.config(menu = instance.unité_selec)


                                instance.gramme = Menu(instance.unité_selec, tearoff=0)

                                def mg():
                                    instance.unité.config(text = "mg")
                                def cg():
                                    instance.unité.config(text = "cg")
                                def dg():
                                    instance.unité.config(text = "dg")
                                def g():
                                    instance.unité.config(text = "g")
                                def dag():
                                    instance.unité.config(text = "dag")
                                def hg():
                                    instance.unité.config(text = "hg")
                                def kg():
                                    instance.unité.config(text = "kg")

                                instance.gramme.add_cascade(label = "kg", command = kg)
                                instance.gramme.add_cascade(label = "hg", command = hg)
                                instance.gramme.add_cascade(label = "dag", command = dag)
                                instance.gramme.add_cascade(label = "g", command = g)
                                instance.gramme.add_cascade(label = "dg", command = dg)
                                instance.gramme.add_cascade(label = "cg", command = cg)
                                instance.gramme.add_cascade(label = "mg", command = mg)
                                instance.unité_selec.add_cascade(menu=instance.gramme, label = "gramme")
                                instance.unité_selec.add_separator()


                                instance.litre = Menu(instance.unité_selec, tearoff=0)
                                def ml():
                                    instance.unité.config(text = "ml")
                                def cl():
                                    instance.unité.config(text = "cl")
                                def dl():
                                    instance.unité.config(text = "dl")
                                def l():
                                    instance.unité.config(text = "l")
                                def dal():
                                    instance.unité.config(text = "dal")
                                def hl():
                                    instance.unité.config(text = "hl")
                                def kl():
                                    instance.unité.config(text = "kl")

                                instance.litre.add_cascade(label = "kl", command = kl)
                                instance.litre.add_cascade(label = "hl", command = hl)
                                instance.litre.add_cascade(label = "dal", command = dal)
                                instance.litre.add_cascade(label = "l", command = l)
                                instance.litre.add_cascade(label = "dl", command = dl)
                                instance.litre.add_cascade(label = "cl", command = cl)
                                instance.litre.add_cascade(label = "ml", command = ml)
                                instance.unité_selec.add_cascade(menu=instance.litre, label = "litre")
                                instance.unité_selec.add_separator()

                                def unité():
                                    instance.unité.config(text = "unité")
                                
                                instance.unité_selec.add_cascade(label = "unité", command = unité)

                                def cuilleres():
                                    instance.unité.config(text = "cuillers à soupe")

                                instance.unité_selec.add_cascade(label = "cuillers à soupe", command = cuilleres)

                                def cuillerec():
                                    instance.unité.config(text = "cuillers à café")

                                instance.unité_selec.add_cascade(label = "cuillers à café", command = cuillerec)

                                def rien():
                                    instance.unité.config(text = "-")

                                instance.unité_selec.add_cascade(label = "-", command = rien)




                                a.bouton[1].append([instance.endroitmenu2, instance.unité] )
                                produit = Text(selection, height=1, width= 20)
                                produit.place(x = x, y=y + 40+30*a.compteur)
                                a.bouton[2].append(produit)
                                a.compteur += 1
                            instance.boutou_plus = Button(selection, text = " + ", font =("", "15"), activebackground= "light blue", bd = 2, relief= "raised", command= lambda : add_infrédient(x,y,instance))
                            instance.boutou_plus.place(x=x+0, y=y+0)

                            def retirer_ingrédient(a):
                                if not a.compteur == 0:
                                    a.bouton[0][-1].destroy()
                                    del a.bouton[0][-1]
                                    a.bouton[1][-1][0].destroy()
                                    del a.bouton[1][-1]
                                    a.bouton[2][-1].destroy()
                                    del a.bouton[2][-1]
                                    a.compteur -= 1
                            instance.boutou_moin = Button(selection, text = " - ", font =("", "15"), activebackground= "light blue", bd = 2, relief= "raised", command= lambda : retirer_ingrédient(instance))
                            instance.boutou_moin.place(x=x+80, y=y+0)
                            def suivant(x,y, instance):
                                instance.data.append([])
                                quantité = []
                                produit = []
                                for i in instance.bouton[0]:
                                    quantité.append(i.get("1.0", END)[:-1])
                                compteur = 0
                                for i in instance.bouton[1]:

                                    quantité[compteur] = quantité[compteur] + " " + i[1].cget("text")
                                    compteur +=1
                                for i in instance.bouton[2]:
                                    produit.append(i.get("1.0", END)[:-1])
                                instance.data[1].append(produit)
                                instance.data[1].append(quantité)
                                for widget in selection.winfo_children():
                                    widget.destroy()


                                instance.selection = selection_du_type(selection,x,y, instance)
                            instance.suivant.config(command = lambda : suivant(x,y, instance))

                    class valider:
                        def __init__(self, selection,  x, y, instance):
                                instance.data = str(instance.data)
                                fichier_text = os.path.abspath(__file__).replace("Création_recette.py", "recette.txt")
                                with open (fichier_text, "r") as f:
                                    contenu = f.read()
                                nouveaux_contenu = contenu.replace("]#END",(",\n" + instance.data + "]#END"))
                                with open(fichier_text, "w") as f:
                                    f.write(nouveaux_contenu)
                                selection.destroy()

