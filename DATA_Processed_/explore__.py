import pandas as pd

# URL du fichier CSV
url = "https://raw.githubusercontent.com/louiskuhn/IA-P3-Euskadi/main/Projets/Projet%20P5%20-%20IMDB/5000_movies_bis.csv"
df = pd.read_csv(url)

# bools par colonne
bool_count = df.select_dtypes(include='bool').sum()
colonnes_a_enlever = bool_count[bool_count == df.shape[0]].index
df = df.drop(columns=colonnes_a_enlever)

colonnes_a_supprimer = ['movie_imdb_link', 'color', 'language', 'country','actor_1_name','actor_2_name','actor_3_name', 'director_name', 'genres', 'movie_title']
df = df.drop(columns=colonnes_a_supprimer)


# NaN par colonne
nan_count = df.isnull().sum()

# colonnes moins de 100 valeurs NaN
colonnes_a_garder = nan_count[nan_count <= 100].index
df = df[colonnes_a_garder]



# supprimer les NaN
df = df.dropna()# netttoyer les  bools
colonnes_a_garder_cleaned = [col for col in df.columns if df[col].dtype != bool]
df_cleaned = df[colonnes_a_garder_cleaned]

# colonnes catégorielles en variables numériques
df_cleaned = pd.get_dummies(df_cleaned)

# colonne "imdb_score" en numérique
df_cleaned['imdb_score'] = pd.to_numeric(df_cleaned['imdb_score'], errors='coerce')


# colonnes avec du texte (type 'object')
colonnes_texte = df.select_dtypes(include=['object']).columns


# nettoyage de la colonne "imdb_score"
nb_lignes_apres_nettoyage_imdb_score = df_cleaned.shape[0]
print("Nombre de lignes après nettoyage de la colonne 'imdb_score' : ", nb_lignes_apres_nettoyage_imdb_score)

# nombre de lignes restantes 
nb_lignes_apres_nettoyage_total = df_cleaned.shape[0]
print("Nombre de lignes restantes après nettoyage total : ", nb_lignes_apres_nettoyage_total)
print(df_cleaned)
print(df.info)

# Sauvegarder le DataFrame nettoyé dans un fichier CSV
nom_fichier = "5000_movies_processed.csv"
df_cleaned.to_csv(nom_fichier, index=False)

print(f"""
#######################################################################
# Le fichier '{nom_fichier}' a été sauvegardé avec succès #
#######################################################################""")


