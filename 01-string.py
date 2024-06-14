#les types natifs


#les chaines de caracteres
print('Je suis une chaine de caracteres')
#il est consiller d'utiliser les guillemets doubles pour ne pas avoir des problemes 
print("Je suis une chaine de caracteres")

#le caractere d'echappemet antislash \ permet de resoudre le probleme des guillemets simples

print('J\'avais')

#retour a la ligne avec \n
print("Je suis une chaine \n de caracteres")

#On peut etre amener a travailler avec des liens vers des dossiers. pour eviter que le \n et le \t ne soient interpreter, on va tout simp0lement ajouter la lette r avant le debut des ' ou "

#dans ce cas, les \t et \n sera interpreter
print('C:\dossiers\taoufik\nouveau') 

#ici, python ne va pas interpreter ces caracteres
print(r'C:\dossiers\taoufik\nouveau')

#liste des caracteres qui sont interpretés de facon spéciale par python

# \a
# \b
# \f
# \n
# \r
# \t
# \v

