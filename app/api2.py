from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from .StoreArtefatosClicados import StoreArtefatosClicados
app = FastAPI()

# Configura o diretório de templates
templates = Jinja2Templates(directory="app/templates")
store = {}

dados = {
        "nome": "Exemplo",
        "email": "exemplo@email.com",
        "mensagem": "Mensagem de exemplo",
        "clique":0
    }

qtd_clique = 0

def escreve(ACC_QTDBTN):
    val_armazenado = ler()
    with open("acumulador.txt", "w") as arq:
        if ACC_QTDBTN != "":
            ACC_QTDBTN += int(val_armazenado)
            arq.write(str(ACC_QTDBTN))


def ler():
    with open("acumulador.txt", "r") as arq:
        ACC_QTDBTN = arq.read().strip() 
    print("valor lido: ",ACC_QTDBTN)
    return ACC_QTDBTN 


@app.post("/enviar-formulario/")
async def receber_formulario(request: Request,nome: str = Form(...), email: str = Form(...), mensagem: str = Form(...), clique: int = Form(...)):
    global dados
    if clique :
        escreve(clique)
    dados = {
        "nome": nome,
        "email": email,
        "mensagem": mensagem,
        "clique":ler(),
    }

    # Redirecionar para a página HTML com os dados
    return templates.TemplateResponse("resultado.html", {"request": request, "dados": dados})

@app.get("/qtd-form/{clique}")
async def relat_clique(request: Request, clique:int, nomebotao:str=None):
    # global qtd_clique
    global store 
    if nomebotao not in store:
        strartc = StoreArtefatosClicados()
        strartc.nomeBotao = nomebotao
        store[strartc.__str__()] = strartc
        store[strartc.__str__()].qtd_clique +=clique
        return templates.TemplateResponse("qtd_cliques.html", {"request": request, "dados": store[strartc.__str__()] ,})
    else:
        print("já existe ,criar logica aqui: ",store)
        store[nomebotao].qtd_clique +=clique
        return templates.TemplateResponse("qtd_cliques.html", {"request": request, "dados": store[nomebotao] ,})


@app.get("/resultado/", response_class=HTMLResponse)
async def exibir_resultado(request: Request):
    global dados
    dados['clique'] =ler()
    return templates.TemplateResponse("resultado.html", {"request": request, "dados": dados,})

