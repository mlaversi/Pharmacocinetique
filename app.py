import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Fonction pour calculer les données
def calculate_data(k_pharma, k_tumeur, k_resistance, k_toxicite, C0):
    dt = 0.1
    t_max = 100.0
    t = [0]
    C = [C0]
    tumeur = [1.0]
    resistance = [0.0]

    while t[-1] < t_max:
        dCdt = -k_pharma * C[-1]**2
        C_new = C[-1] + dCdt * dt

        dTdt = k_tumeur * C[-1] - 0.01 * tumeur[-1] - k_toxicite * C[-1] * tumeur[-1] * (1 - resistance[-1])
        tumeur_new = tumeur[-1] + dTdt * dt

        dRdt = k_resistance * C[-1] * tumeur[-1] * (1 - resistance[-1])
        resistance_new = resistance[-1] + dRdt * dt

        t.append(t[-1] + dt)
        C.append(C_new)
        tumeur.append(tumeur_new)
        resistance.append(resistance_new)

    return t, C, tumeur, resistance

# Titre de l'application
st.title('Modèle de Pharmacocinétique')


st.write('Comment la dose initiale du médicament (C0) (Adriamycine) affecte-t-elle la croissance de la tumeur et le développement de la résistance au fil du temps?')

st.write("Prenons l'exemple d'un médicament couramment utilisé qui est l'Adriamycine ou (doxorubicine). C'est un médicament de chimiothérapie largement prescrit pour le traitement de divers types de cancer, notamment le cancer du sein, le lymphome, le sarcome des tissus mous et d'autres cancers. Veuillez noter que l'utilisation de médicaments de chimiothérapie doit être strictement supervisée par un professionnel de la santé")
# Texte introductif
st.write("""
Dans cette application, nous explorons un modèle pharmacocinétique qui étudie l'interaction d'un médicament avec une tumeur. Le modèle comprend les équations suivantes :

1. **Équation de Pharmacocinétique :**
   - `dC/dt = -k_pharma * C^2`
   - Cette équation décrit la variation de la concentration du médicament (C) dans le temps en fonction de la constante de pharmacocinétique (k_pharma).

2. **Équation de Croissance de Tumeur :**
   - `dT/dt = k_tumeur * C - 0.01 * tumeur - k_toxicite * C * tumeur * (1 - resistance)`
   - Cette équation modélise la croissance de la tumeur (tumeur) en réponse à la concentration du médicament (C), avec des termes de croissance, de décroissance et de toxicité.

3. **Équation de Résistance de Tumeur :**
   - `dR/dt = k_resistance * C * tumeur * (1 - resistance)`
   - Cette équation représente l'évolution de la résistance de la tumeur (résistance) en réponse à la concentration du médicament (C) et à la taille de la tumeur (tumeur).

En utilisant cette application, vous pouvez ajuster les paramètres (k_pharma, k_tumeur, k_resistance, k_toxicite, C0) et observer comment ils affectent la concentration du médicament, la taille de la tumeur et la résistance de la tumeur au fil du temps.

Essayez de modifier les paramètres pour comprendre comment différentes conditions influent sur l'efficacité du médicament et l'évolution de la tumeur. A noter que ceci est une représentation très simplifié de la pharmacocinétique. 
""")

# Widgets pour les paramètres
k_pharma = st.slider('k_pharma', 0.0, 1.0, 0.1)
k_tumeur = st.slider('k_tumeur', 0.0, 1.0, 0.01)
k_resistance = st.slider('k_resistance', 0.0, 1.0, 0.002)
k_toxicite = st.slider('k_toxicite', 0.0, 1.0, 0.002)
C0 = st.slider('C0', 0.0, 2.0, 1.0)

# Bouton pour recalculer les données
if st.button('Calculer'):
    # Calculer les données
    t, C, tumeur, resistance = calculate_data(k_pharma, k_tumeur, k_resistance, k_toxicite, C0)

    # Afficher le graphique avec les données calculées
    st.line_chart({'Concentration du médicament': C, 'Taille de la tumeur': tumeur, 'Résistance de la tumeur': resistance})
    