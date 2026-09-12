import json

'''Permet de charger le fichier json et ouvrir la liste des observations'''

def charger_fichier(chemin_fichier:str) -> list[dict]:
    chemin=Path(chemin_fichier) 
    if not chemin.exists():
        print("Chemin introuvable")
        sys.exit(1)
    with chemin.open("r", encoding="utf-8") as f:
        donnees=json.load(f)
    
    return donnees

