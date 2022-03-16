from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Trabalho IAC", openapi_url = None)

class Mensagem(BaseModel):
    message: str

knowledge_dict = {
        " ":" Me pergunte algo",
        "ola":"Ola, tudo bem?",
        "tudo bem?":"Sim, esta tudo bem",
        "sim, e com voce?":"Tudo bem.",
        "sim, estou bem":"Que bom!",
        "bom dia":"Oi, bom dia para você também!",
        "boa tarde":"Oi, boa tarde para você também!",
        "boa noite":"Oi, boa noite para você também!",
        "estou triste":"Sinto muito, o que houve?",
        "estou feliz":"Legal, isso e muito bom",
        "como voce esta?":"Estou bem, e voce?",
        "voce gosta musica?":"Sim, minha cantora favoria e Camila Cabello"
        
    }


def _get_answer(question: str) -> str:
    return knowledge_dict.get(question.lower())

@app.get("/", tags=["Robô de fala"], include_in_schema=False)
def home():
    return {
        "resposta":"Bem vindo ao robô de fala! Para saber como usar minhas funções entre no link https://trabalho-iac.herokuapp.com/docs"
    }

@app.get("/conhecimento", tags=["Robô de fala"])
def knowledge():
    known_questions = [] 
    for k in knowledge_dict:
        known_questions.append(k)
    
    return {
        "coisas_que_sei":known_questions
    }


@app.post("/ask_something", tags=["Robô de fala"])
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




