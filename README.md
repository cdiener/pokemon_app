<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/International_Pok%C3%A9mon_logo.svg/1200px-International_Pok%C3%A9mon_logo.svg.png" width="60%">

Esqueleto para un simple servicio que predice que Pokemon gana en una pelea.

La app nada más tiene una direccion/route a la raiz (por ejemplo
http://localhost:5000). Datos se pasan con un request the POST con
un cuerpo de JSON.

### Por ejemplo:

input:

```JSON
{
    "pokemon 1": "Pikachu",
    "pokemon 2": "Bulbasaur"
}
```

Después de mandarlo con un request the POST a http://localhost:5000 recibes

output:
```JSON
{
    "pokemon 1": "Pikachu",
    "pokemon 2": "Bulbasaur",
    "winner": "Bulbasaur",
    "confidence": 0.85
}
```

# Requisitos para correrlo

- Python 3.4+
- Flask
- py.test

Instala lo con `pip3 install --user -r requirements.txt`

# Como correr la App

```bash
python3 app.py
```

Esto expone tu app para la direccion http://localhost:5000. Lo puedes probar
con [curl](https://es.wikipedia.org/wiki/CURL)  o usand puro python con la
librería de requests:

```python
response = requests.post("http://localhost:5000",
                         json={"pokemon 1": "Pikachu", "pokemon 2": "Bulbasaur"})

response.status_code
# 400

response.json()
# {'error': 'not implemented yet!'}
# también puedes usar response.text
```

# Obtener tu puntaje

```bash
py.test test_app.py
```

Tu puntaje es el numero de pruebas pasadas.
