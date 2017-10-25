"""Entrena el modelo para la Pokemon App.

Usamos una formulación binaria (el primer Pokemon gana o no) con todos
los stats de los dos Pokemones como variables. Tienes que correr este archivo
al menos una vez antes que corres la app.

> python3 train.py
"""

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle

# Vamos a leer los datos. Para los estadisticas de los Pokemones usamos
# la primera columna como index (ID del Pokemon).
combats = pd.read_csv("combats.csv")
pokemon = pd.read_csv("pokemon.csv", index_col=0)

# Separamos los variables categoricas y continuas y aplicamos el
# pre-procesamiento. One-hot encoding para los categoricas y
# estandardización para los continuas.
cat = pokemon[["Type 1", "Type 2", "Legendary"]]
cat = pd.get_dummies(cat, drop_first=True)
cont = pokemon.drop("Name", axis=1).iloc[:, 3:10]
scaler = StandardScaler().fit(cont)
cont = pd.DataFrame(scaler.transform(cont), index=pokemon.index)

# Unimos las variables otra vez.
stats = pd.concat([cat, cont], axis=1)  # np.hstack([matrix1, matrix2])

# Ahora sacamos las stats para el primer y segundo Pokemon
# para cada pelea. Tenemos que reiniciar el index para unirlos mas tarde.
first = stats.loc[combats.First_pokemon].reset_index(drop=True)
second = stats.loc[combats.Second_pokemon].reset_index(drop=True)

# Finalmente unimos las variables y asignamos la respuesta para el
# entrenamiento.
train = pd.concat([first, second], axis=1)
response = combats.First_pokemon == combats.Winner

# Entrenamos un Random Forest y usamos el OOB score (exactitud) para
# ver que bueno funciona.
clf = RandomForestClassifier(100, n_jobs=4, oob_score=True)
clf.fit(train, response)
print("OOB estimate:", clf.oob_score_)

# Ahora vamos a guardar el modelo para la app.
with open("model.pickle", "wb") as out:
    pickle.dump(clf, out)

# También guardamos los stats juntos con los nombres de los Pokemones.
stats["pokename"] = pokemon.Name
stats.to_pickle("stats.pickle")
