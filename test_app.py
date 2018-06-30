"""Evalua tu API."""

import pytest
import json
import pandas as pd
from app import app as pokemon_app

combats = pd.read_csv("combats.csv").sample(100).reset_index(drop=True)
pokemon = pd.read_csv("pokemon.csv", index_col=0)
combats.First_pokemon = pokemon.Name.loc[
    combats.First_pokemon].reset_index(drop=True)
combats.Second_pokemon = pokemon.Name.loc[
    combats.Second_pokemon].reset_index(drop=True)
combats.Winner = pokemon.Name.loc[combats.Winner].reset_index(drop=True)

@pytest.fixture
def app():
    return pokemon_app.test_client()


def post_json(app, data):
    """Post a dictionary as JSON to the app."""
    return app.post("/", data=json.dumps(data),
                    content_type="application/json")


good_inputs = [
    {"pokemon 1": "Pikachu", "pokemon 2": "Bulbasaur"},
    {"pokemon 1": "Tangela", "pokemon 2": "Rhydon"},
    {"pokemon 1": "Volcanion", "pokemon 2": "Weedle"}
]

bad_inputs = [
    {"pokemon 1": "Pikachu", "pokemon 2": "Bulbasaurus"},
    {"pokemon 1": "Tangela", "pokemon 3": "Rhydon"},
    {"pika": "pikapika"}
]

good_response = {
    "pokemon 1": "Pikachu",
    "pokemon 2": "Bulbasaur",
    "winner": "Bulbasaur",
    "confidence": 0.85
}


def test_api_returns_json(app):
    resp = post_json(app, good_inputs[0])
    assert resp.mimetype == "application/json"


@pytest.mark.parametrize("body", good_inputs)
def test_good_inputs(app, body):
    resp = post_json(app, body)
    assert resp.status_code == 200
    assert resp.mimetype == "application/json"


@pytest.mark.parametrize("body", bad_inputs)
def test_bad_inputs(app, body):
    resp = post_json(app, body)
    assert resp.status_code == 400


@pytest.mark.parametrize("body", good_inputs)
def test_response_format(app, body):
    resp = post_json(app, body)
    data = json.loads(resp.get_data(True))
    assert all(k in data for k in good_response)


def test_predict_winners(app):
    correct = 0
    for _, r in combats.iterrows():
        body = {"pokemon 1": r.First_pokemon, "pokemon 2": r.Second_pokemon}
        resp = post_json(app, body)
        data = json.loads(resp.get_data(True))
        correct += data["winner"] == r.Winner
    assert correct >= 97
