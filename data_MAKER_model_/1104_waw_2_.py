import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Charger le fichier CSV
df = pd.read_csv('/home/shaney/Bureau/_IBM_PREDICT_/data/5000_movies_processed.csv')

# vérifier qu'il y a tout ce qu'on cherche
print(df.columns)

# si 'imdb_score' est présent 
if 'imdb_score' in df.columns:
    # X & y
    X = df.drop(columns=['imdb_score'])
    y = df['imdb_score']

    random_state = 42 
    test_size = 0.2 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    modele = LinearRegression()
    modele.fit(X_train, y_train)
    predictions = modele.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    nom_modele = f"_modele_waw_{mse:.4f}.joblib"
    joblib.dump(modele, nom_modele)

    # Afficher le nom du modèle enregistré
    print(f"Modèle enregistré sous: {nom_modele}")
else:
    print("La colonne 'imdb_score' n'est pas présente dans le DataFrame.")
