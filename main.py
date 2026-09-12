import json

'''Permet de charger le fichier json et ouvrir la liste des observations'''

def charger_fichier(chemin_fichier:str) -> list[dict]: '''Transforme le texte en liste de dictionnaire (plus simple a manipuler ig)'''
    chemin=Path(chemin_fichier) 
    if not chemin.exists():
        print("Chemin introuvable")
        sys.exit(1)
    with chemin.open("r", encoding="utf-8") as f:
        donnees=json.load(f)
    
    return donnees

def calc_vitesse(observations: list[dict]) -> list[dict]:
    for obs_precedente, obs_suivante in zip(observations, observations[1:]): '''zip -> paires consecutives du style (obs[2],obs[3])'''