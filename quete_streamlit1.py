import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib


st.title('Voici mon analyse!')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)

df["continent"] = df["continent"].apply(lambda x : x.replace(".", ""))

option = st.selectbox(label= "veuillez séléctionner un continent.", options= df["continent"].unique())

st.write('You selected:', option)

new_df = df[df["continent"]== option]

st.write("Voici mon analyse en fonction du continent séléctionné")


#mes graph :

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(30, 23))

ax1 = sns.barplot(data= new_df, x="continent", y="hp", ax=axs[0, 0])
ax1.set_title("Le nombre de cylindre par continent", fontsize=20)  # Modifie la taille du titre du subplot
ax1.set_xlabel("Continent", fontsize=20)  # Modifie la taille de l'étiquette de l'axe des abscisses
ax1.set_ylabel("Nombre de cylindre", fontsize=20)  # Modifie la taille de l'étiquette de l'axe des ordonnées

ax2 = sns.lineplot(data= new_df, x="year", y="hp", hue="continent", ax=axs[0, 1])
ax2.set_title("L'évolution de la puissance dans le temps par continent", fontsize=20)
ax2.set_xlabel("Année", fontsize=20)
ax2.set_ylabel("Puissance", fontsize=20)

ax3 = sns.scatterplot(data= new_df, x="hp", y="weightlbs", hue="continent", s=100, ax=axs[1, 0])
ax3.set_title("Le poids en fonction de la puissance par continent", fontsize=20)
ax3.set_xlabel("Puissance", fontsize=20)
ax3.set_ylabel("Poids", fontsize=20)

ax4 = sns.scatterplot(data= new_df, x="weightlbs", y="mpg", hue="continent",s=100, ax=axs[1, 1])
ax4.set_title("La consomation en fonction du poid par continent", fontsize=20)
ax4.set_xlabel("poid (lbs)", fontsize=20)
ax4.set_ylabel("miles par gallon", fontsize=20)

st.pyplot(ax1.figure)

st.write("Voici mon analyse permettant la comparaison entre les différent continent")

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(30, 23))

ax1 = sns.barplot(data= df, x="continent", y="hp", ax=axs[0, 0])
ax1.set_title("Le nombre de cylindre par continent", fontsize=20)  # Modifie la taille du titre du subplot
ax1.set_xlabel("Continent", fontsize=20)  # Modifie la taille de l'étiquette de l'axe des abscisses
ax1.set_ylabel("Nombre de cylindre", fontsize=20)  # Modifie la taille de l'étiquette de l'axe des ordonnées

ax2 = sns.lineplot(data= df, x="year", y="hp", hue="continent", ax=axs[0, 1])
ax2.set_title("L'évolution de la puissance dans le temps par continent", fontsize=20)
ax2.set_xlabel("Année", fontsize=20)
ax2.set_ylabel("Puissance", fontsize=20)

ax3 = sns.scatterplot(data= df, x="hp", y="weightlbs", hue="continent", s=100, ax=axs[1, 0])
ax3.set_title("Le poids en fonction de la puissance par continent", fontsize=20)
ax3.set_xlabel("Puissance", fontsize=20)
ax3.set_ylabel("Poids", fontsize=20)

ax4 = sns.scatterplot(data= df, x="weightlbs", y="mpg", hue="continent",s=100, ax=axs[1, 1])
ax4.set_title("La consomation en fonction du poid par continent", fontsize=20)
ax4.set_xlabel("poid (lbs)", fontsize=20)
ax4.set_ylabel("miles par gallon", fontsize=20)

st.pyplot(ax1.figure)

plt.figure(figsize=(20,15))

heatmap = sns.heatmap(df.corr(numeric_only=True),
                  center=0,
                  cmap=sns.color_palette("vlag", as_cmap=True),
                  annot=True, vmin=-1)
heatmap.set_title("Les différentes corrélations entre chaque série de données", fontsize=20)
heatmap.set_xlabel("Caractéristiques", fontsize=20)
heatmap.set_ylabel("Caractéristiques", fontsize=20)

st.write("Voici une carte de chaleur permettant d'avoir une vision global sur les corrélation entre les séries de données")

st.pyplot(heatmap.figure)







