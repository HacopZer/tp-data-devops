import pandas as pd 

  

from pipeline import agreger_par_ville, agreger_par_categorie, transformer

  

  

def donnees_exemple(): 

    return pd.DataFrame({ 

        "quantite": [2, 2, None, -1, 3], 

        "prix_unitaire": [10.0, 10.0, 5.0, 5.0, 20.0], 

        "ville": ["paris", "paris", "Lyon", "Lyon", " lyon"], 

    }) 

  

  

def test_supprime_les_doublons_et_lignes_invalides(): 

    resultat = transformer(donnees_exemple()) 

    assert len(resultat) == 2 

  

  

def test_normalise_les_villes(): 

    resultat = transformer(donnees_exemple()) 

    assert sorted(resultat["ville"]) == ["Lyon", "Paris"] 

  

  

def test_calcule_le_montant(): 

    resultat = transformer(donnees_exemple()) 

    assert resultat["montant"].sum() == 80.0 

  

  

def test_agregation_par_ville(): 

    resultat = agreger_par_ville(transformer(donnees_exemple())) 

    assert resultat.iloc[0]["ville"] == "Lyon" 

    assert resultat.iloc[0]["montant"] == 60.0 


def test_agregation_par_categorie():
    # Petit jeu de données construit à la main
    df = pd.DataFrame({
        "categorie": ["Informatique", "Mobilier", "Informatique"],
        "montant": [100.0, 50.0, 20.0],
    })

    resultat = agreger_par_categorie(df)

    # Calcul à la main : Informatique = 100 + 20 = 120 ; Mobilier = 50
    attendu = {"Informatique": 120.0, "Mobilier": 50.0}
    assert dict(zip(resultat["categorie"], resultat["montant"])) == attendu

    # Tri décroissant : la catégorie au plus gros CA vient en premier
    assert resultat.iloc[0]["categorie"] == "Informatique"