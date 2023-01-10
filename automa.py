import requests
import json


# API
api = requests.get("https://ws.smn.gob.ar/map_items/weather")
json_data = json.loads(api.content)


def tiempo_ciudad(ciudad):
    # import pdb;pdb.set_trace()
    # ciudad = json_data[0]["province"]
    estado_cielo = ""
    temperatura = ""

    for ciudad_data in json_data:
        if ciudad_data["province"] == ciudad:
            # import pdb;pdb.set_trace()
            estado_cielo = ciudad_data["weather"]["description"]
            temperatura = ciudad_data["weather"]["tempDesc"]

    texto_final = (
        f"Luli, recorda regar las plantas. Aca tenes una prediccion de hoy en {ciudad} \nCielo{estado_cielo} Temperatura {temperatura}"
    )

    return texto_final


tiempo = tiempo_ciudad("Buenos Aires")

requests.post(
    "https://api.telegram.org/bot5882569616:AAF6UbPelAZhiq5ebB1o-IFPHH_5VcxT8MI/sendMessage",
    data={"chat_id": "@RecordaRegado", "text": tiempo},
)
