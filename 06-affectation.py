#affectation simple
a = 5
b = 8

# affectation parallèle
a,b = 5,8
# cette maniere est principalement utilisée pour inverser les valeurs de deux variables
a,b = b,a

# pour l'affectation parallele, il n'y a pas de limite de variable. la seule limite c'est la lisibilité

#les affectation miultiples. 
#Elles sont utilisé lorceque nos variables ont la meme valeur

a = b = c = 5

#ATTENTION. POUR LES AFFECTATIONS MULTIPLES, ON DOIS TOUJOUR TERMINER NOTRE AFFECTATION PAR LA VALEUR QU'ON VEUT ATTRIBUER AUC TROIS VARIABLES


#Changer le type de la variable

"""
    On change le type d'une variable pour:
    -utiliser les operateurs mathematiques
    -Comparer deux variables entre elles. en python, 50 != "50"
"""
a = "20"
a = int(a)

#Ne jamais se fier au visuel. il faut toujours verifier le type de la variable
print(type(a))
#<class 'int'> ici, a est une instance de la classe int




#ATTENTON
#interaction avec un utilisateur
#La fonction input qui permet de recuperer une valeur venamt de l'utilisateur retourne toujour une chaine de caractere

nombre = input("Veuillez saisir un int: ")
print(type(nombre))
"""
    Veuillez saisir un int: 5
    <class 'str'>
"""
 