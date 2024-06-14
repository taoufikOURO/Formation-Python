#On passe un objet en parametre et on va varifier si cet objet est apoeleble ou non 

#On n'appelle pas un module. On ne peut que appeler les fonctions dans le module
from pprint import pprint
import os

print(callable(pprint)) 
print(os.name)
