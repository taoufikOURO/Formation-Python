liste = ["1", "4", "35", "Taoufik", "3", "Badiou"]
for item in liste:
    if item.isdigit(): #si l'element est un nombre, on passe a l'ittération suivante
        continue
    print(item)

for item in liste:
    if item.isdigit(): #si l'element est un nombre, on arrete tout
        break
    print(item)