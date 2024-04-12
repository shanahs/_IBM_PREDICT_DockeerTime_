from flask import Flask, render_template, request
import joblib
import pandas as pd
from sklearn.metrics import r2_score

modele = joblib.load('data__model/_modele_waw_mse_0.9481.joblib')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def accueil():
    if request.method == 'POST':
        # formulaire
        num_critic_for_reviews = float(request.form['num_critic_for_reviews'])
        duration = float(request.form['duration'])
        actor_3_fb_likes = float(request.form['actor_3_fb_likes'])
        actor_1_fb_likes = float(request.form['actor_1_fb_likes'])
        num_voted_users = float(request.form['num_voted_users'])
        cast_total_fb_likes = float(request.form['cast_total_fb_likes'])
        facenumber_in_poster = float(request.form['facenumber_in_poster'])
        num_user_for_reviews = float(request.form['num_user_for_reviews'])
        actor_2_fb_likes = float(request.form['actor_2_fb_likes'])
        movie_fb_likes = float(request.form['movie_fb_likes'])
        
        # valeurs CSV
        csv_values = request.form['csv_values'].strip()
        csv_list = csv_values.split(',')
        valeur_reelle = float(csv_list[-2]) if len(csv_list) >= 2 else None

        # créé un dataframe
        data = {
            'num_critic_for_reviews': [num_critic_for_reviews],
            'duration': [duration],
            'actor_3_fb_likes': [actor_3_fb_likes],
            'actor_1_fb_likes': [actor_1_fb_likes],
            'num_voted_users': [num_voted_users],
            'cast_total_fb_likes': [cast_total_fb_likes],
            'facenumber_in_poster': [facenumber_in_poster],
            'num_user_for_reviews': [num_user_for_reviews],
            'actor_2_fb_likes': [actor_2_fb_likes],
            'movie_fb_likes': [movie_fb_likes]
        }
        df = pd.DataFrame(data)

        # Ffait la prédiction
        try:
            prediction = modele.predict(df)[0]
        except Exception as e:
            prediction = None
            print(f"Erreur lors de la prédiction : {e}")

        # Calculer la précision du modèle (R2 score)
        precision = r2_score([valeur_reelle], [prediction]) * 100 if valeur_reelle is not None and prediction is not None else None

        return render_template('resultat.html', prediction=prediction, valeur_reelle=valeur_reelle, precision=precision)
    else:
        return render_template('acceuil.html')

if __name__ == '__main__':
    # app.run(debug=True)  # pour tester l'app en local
    app.run(host='0.0.0.0')# pour le conteneur
