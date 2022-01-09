from typing import Optional
from pyvi import ViTokenizer, ViPosTagger
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"res": "Homepage"}


@app.get("/tokenize/{sentence}")
def read_item(sentence: str):
    res = ViPosTagger.postagging(ViTokenizer.tokenize(sentence))
    return {"res": res}