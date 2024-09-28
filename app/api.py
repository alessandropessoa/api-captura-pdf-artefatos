from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

# Modelo para os dados do formulário
class Formulario(BaseModel):
    nome: str
    email: str
    mensagem: str

# Rota para receber os dados do formulário via POST
@app.post("/enviar-formulario/")
async def receber_formulario(nome: str = Form(...), email: str = Form(...), mensagem: str = Form(...)):
    return {
        "nome": nome+"Retorno do servido",
        "email": email+"foi modificado",
        "mensagem": mensagem
    }

@app.post("/enviar-formulario/")
async def receber_formulario(nome: str = Form(...), email: str = Form(...), mensagem: str = Form(...)):
    return {
        "nome": nome+"Retorno do servido",
        "email": email+"foi modificado",
        "mensagem": mensagem
    }