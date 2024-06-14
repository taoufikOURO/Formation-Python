#changer la casse des chaines de caracteres
a = "bonjour a tous"

#mettre en lettre capitales
a = a.upper()
print(a)


#mettre en lettre minuscule
a = a.lower()
print(a)


#mettre la premiere lettre en majuscule
a = a.capitalize()
print(a)

#Mettre la premiere lettre de chaque mot en majuscule
a = a.title()
print(a)

#remplacer une partie de la chaine de caractere par une autre chaine de caractere

#attention, il va remplacer toutes les occurences

a = "bonjour a tous".replace("jour", "soir")
print(a)


#la methode strip va nous permettre de supprimer les espaces au debut et a la fin de la chaine de caractere JAMAIS AU BEAU MILIEUR DE LA CHAINE DE CARACTERE
print("  bonjour   ")
print("  bonjour   ".strip())

#Separer et joindre les elements des chaines de caracteres
print("1, 2, 3, 4, 5".split(", "))

#Remplir de 0
#zflill ne marche que sur les chaines de caracteres
print("9".zfill(4))

#la methode is----
print("50".isdigit())

#compter les occurences de caracteres
#il suffit de lui donner une chaine de caractere et elle retourne le nombre d'occurence de cette derniere
print("Bonjour le jour".count(" jour"))



#trouver une chaine
#find va envoyer -1 si il ne trouve pas la chaine decaractere
print("Bonjour le jour".find("jour"))

#on peut partir de droite egalement en ajoutant r pour right
print("Bonjour le jour".rfind("jour"))


#index va renvoyer une erreur
print("Bonjour le jour".index("jour"))

#chercher au debut et a la fin d'une chaine de caractere

print("image.png".endswith(".png"))
print("image.png".endswith(".jpg"))

#on a aussi startwith
print("image.png".startswith("image"))