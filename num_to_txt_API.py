from typing import Annotated
from fastapi import FastAPI, Query
from num_to_text import checagem
app = FastAPI()


@app.get("/Numero_Texto/")
def exibe_numeros(numero_digitado: Annotated[str, Query(max_length=3)]):
    return checagem(numero_digitado)


