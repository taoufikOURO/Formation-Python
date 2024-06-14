import os

chemin = r"C:\Users\ourot\OneDrive\Documents\FORMATION\PYTHON"

dossier = os.path.join(chemin, "dossier", "test")
os.makedirs(dossier, exist_ok=True)

if os.path.exists(dossier):
    os.removedirs(dossier)
else:
    print("Le dossier n'existe pas")
