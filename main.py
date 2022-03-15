from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class Mensagem(BaseModel):
    message: str

def _get_answer(question: str) -> str:
    return {
        " ":" Me pergunte algo",
        "ola":"Ola, tudo bem?",
        "tudo bem?":"Sim, esta tudo bem",
        "sim, e com voce?":"Tudo bem.",
        "sis, estou bem":"Que bom!",
        "bom dia":"Oi, bom dia para você também!",
        "boa tarde":"Oi, boa tarde para você também!",
        "boa noite":"Oi, boa noite para você também!",
        "estou triste":"Sinto muito, o que houve?",
        "estou feliz":"Legal, isso e muito bom",
        "como voce esta?":"Estou bem, e voce?",
        "voce gosta musica?":"Sim, minha cantora favoria e Camila Cabello"
        
    }.get(question.lower())


@app.post("/ask_something")
def ask(msg:Mensagem):
    asw = _get_answer(msg.message)

    if asw != None:
        return {
            "resposta": asw
        }
    else:
        return HTTPException(
            detail="Ainda nao sei o que voce esta falando, por favor me pergunte algo que eu sei",
            status_code= status.HTTP_400_BAD_REQUEST
        )




