import random
from pprint import pprint

#Faire de l'introspection
#Afficher toutes les fonctions un module en particulier
print(dir(random))

#afficher l'aide a propos d'une fonction
#Il faut eviter de mettre les parentheses a la fin des fonctions. On ne veux pas les appeler. on vaux juste des infos sur la fonction
help(random.randint)

#la fonction pprint permet de mieux afficher le bye

pprint(dir(random))