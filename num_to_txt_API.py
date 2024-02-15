from fastapi import FastAPI
from pydantic import BaseModel
from tinydb import TinyDB, Query
from num_to_text import checagem

db = TinyDB("numeros.json")
user = Query()

app = FastAPI()


class Numero(BaseModel):
    numero: int


@app.post("/numeros/")
# Salvar no banco de dados
def salvar_no_banco(numeros: Numero):
    return "Numero adicionado ao banco de dados"


@app.get("/Mostrar_Numero")
# Mostrar numeros salvos
def exibe_numero_texto():
    return
