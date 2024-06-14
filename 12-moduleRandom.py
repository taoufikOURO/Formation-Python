#Quelques modules de la librairie standard de python
import random

#Recuperer un nombre int aléatoire
r = random.randint(0,2)
print(r)

#Recuperer une valeur decimale
r = random.uniform(0, 1)
print(r)

#randrange fonctionne comme randint mais avec un seul parametre
#ici c'est exclusif. le 20 n'est pas compris. Ce qui est une ditterence avec randint
r = random.randrange(20)
print(r)

