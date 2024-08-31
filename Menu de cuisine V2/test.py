import os   
fichier_text = os.path.abspath(__file__).replace("test.py", "recette.txt")                             
with open (fichier_text, "r") as f:
                                    contenu = f.read()
print(contenu)
                                
nouveaux_contenu = contenu.replace("",(""))
with open(fichier_text, "w") as f:
        f.write(nouveaux_contenu)