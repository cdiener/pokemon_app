"""App para predecir quien gana en una pelea de Pokemon.

La app nada más tiene una direccion/route a la raiz (por ejemplo
http://localhost:5000). Datos se pasan con un request the POST con
un cuerpo de JSON.

Por ejemplo:

input -> {"pokemon 1": "Pikachu", "pokemon 2": "Bulbasaur"}

output -> {
              "pokemon 1": "Pikachu",
              "pokemon 2": "Bulbasaur",
              "winner": "Bulbasaur",
              "confidence": 0.85
          }
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
app.secret_key = "pikapika"


def winner(pokemon1, pokemon2):
    """Determina quien gana y con que confianza."""
    # Tu codigo aquí
    return None


@app.route("/", methods=["GET", "POST"])
def get_winner():
    """Accesso a la API REST.

    El body del request debería contener los pokemones que
    compiten. Para funcionar perfecto debería dar los siguiente
    codigos de estatus:

    metodo GET
    ----------
    200 con un mensaje motivador

    metodo POST
    -----------
    - 200 con la respuesta para input correcto
    - 400 con un mensaje de error para input malformado

    """
    body = request.get_json()
    # Tu codigo aquí
    return jsonify(error="not implemented yet!"), 400


if __name__ == "__main__":
    app.run(debug=True)
