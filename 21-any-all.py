#any
#retoutne vrai si un seul element dans la liste est vrai

print(any([False, False, True, False])) 


#all
#Retourne vrai si tous les elements de la lisyte sont vrai
print(all([False, False, True, False])) 

#Il est tres rare de passer directement des booleens

files = ["image.jpg", "Taoufik.jpg", "tao.jpeg"]
all([f.endswith(".jpg") for f in files])