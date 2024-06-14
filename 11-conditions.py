#Condition if
age = input("Veuillez saisir votre age: ")
try:
    age = int(age)
    if(age >= 18):
        print("Vous etes majeur")
    else:
        print("Vous etes un mineur")
except:
    print("veuillez saisir un nombre. Pas des lettres")

#les operateurs ternaires
majeur = ""
majeur = True if age >=18 else False


#les operateurs logiques OR, AND et NOT
