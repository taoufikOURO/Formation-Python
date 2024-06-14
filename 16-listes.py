liste = []

#Ajouter des elements a une liste
#une seule valeur a la fois
liste.append("taoufik")

#plusieurs valeurs a la fois sous forme de liste
liste.extend(["Taoufik", "Badiou", "Jamil", "Sam", "Ahmed", "Az", "Zia"])
print(liste)

#retirer un elment
#elle retire la premiere occurence de l'element
liste.remove("taoufik")
print(liste)

#recuperer un element dans une liste
#les indicers commencent par 0
#on peut recuperer le dernier element en commencant par -1
print(liste[0])
print(liste[-1])


#les slices pour decouper une liste
# le dernier element est exclusif
print(liste[0:2])

#on peut imposer le pas aussi
#on commence a l'index 1, jusqu'a la fin avec un pas de 2
print(liste[1::2])


#methodes sur les listes
#connaitre l'index d'un element dans la liste
print(liste.index("Taoufik"))

#compter le mombre d'occurence d'un element dans la liste
print(liste.count("Taoufik"))

#ranger une liste par ordre alphabétique
#la methode sort ne retourne rien. Elle trie juste la liste.
#le print va retourner NONE
print(liste.sort())
# NE JAMAIS FAIRE liste = liste.sort()

#inverser l'order de la liste. Pas un tri dans l'order décroisant
#le print va retourner NONE
print(liste.reverse())

#supprimer un element par rapport a son index
liste.pop(1)
print(liste)

#Joindre les elements d'une liste
#Ca ne marche que avec les chaines de carateres
resultat = " ".join(liste)
print(resultat)

#transformer une chaine de caractere en liste
phrase = "Mon nom est OURO-BANG'NA Taoufik et je suis en deuxieme année"
#il va spliter sur les espaces si il n'y a pas d'arguments
#l'argument sera le separateur
phrase = phrase.split()
print(phrase)

#les opereateurs
#verifier si un element est present dans une liste
#il faut faire attention a la casse
if "Zia" in liste:
    print("Zia est dans la liste")

#Les listes imbriqués
liste_imbr = ["Python",["Java", "PHP", "Javascript"], ["Swift", "Kotlin", "Flutter"]]
print(liste_imbr[1][0]) #va me retourner Java


#la fonction len.
#va nous retourner le nombre de valeur dans une liste
a = len(liste_imbr)
print(a)

#recuperer la valeur max et la valeur min
notes = [10, 12, 11, 14, 17, 13, 12, 19, 14]
print(max(notes)) #le minimum
print(min(notes)) #le maximum

#la somme des elements dans une liste
#Uniquement possible sur des nombres
somme = sum(notes)
print(somme)