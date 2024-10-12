import streamlit as st
import pandas as pd
from prediction import load_model, make_predictions 

st.title("Prédiction de l'espèce d'une fleur Iris 🌸")
st.write("""
    Cette application utilise un modèle d'apprentissage automatique pour prédire l'espèce d'une fleur
    Iris en fonction de la longueur et largeur de ses sépales et pétales.
""")

# Diviser en deux colonnes pour une meilleure présentation
col1, col2 = st.columns(2)

# Colonnes pour les sliders des caractéristiques de la fleur
with col1:
    sepal_length = st.slider("Longueur des sépales (cm)", 4.0, 8.0, 5.0)  # Slider pour la longueur des sépales
    sepal_width = st.slider("Largeur des sépales (cm)", 2.0, 4.5, 3.0)   # Slider pour la largeur des sépales

with col2:
    petal_length = st.slider("Longueur des pétales (cm)", 1.0, 7.0, 4.0)  # Slider pour la longueur des pétales
    petal_width = st.slider("Largeur des pétales (cm)", 0.1, 2.5, 1.0)   # Slider pour la largeur des pétales

model_path = "C:/Users/Home/Desktop/ids5/TP1_MLOPS_Streamlit/decision_tree_model.joblib"
model = load_model(model_path)

# Étape 5 : Fonction pour lancer la prédiction
if st.button("Prédire l'espèce de la fleur"):
    # Créer un DataFrame avec les caractéristiques d'entrée
    input_data = pd.DataFrame({
        "sepal_length": [sepal_length],
        "sepal_width": [sepal_width],
        "petal_length": [petal_length],
        "petal_width": [petal_width]
    })
    
    # Appel à la fonction de prédiction (depuis prediction.py)
    prediction = make_predictions(model, input_data)

    # Afficher le résultat de la prédiction
    st.success(f"L'espèce prédite est : {prediction[0]}")
