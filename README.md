Este projeto é um esboço inicial de como rastrear cliques em artefastos pdfs ("botões que foram clicados"), desta forma é possivel
se ter uma ideia de leads que interagiram com o pdf. 
O app quando em sua fase completa deve ser cpaz de rastrear os artefatos, que podem ser desde botões clicaveis até
os campos interativos do pdf, neste sentido deve-se adicionar JS no pdf e entender que pode gaver limitaçoes
quanto a captura desse dados devido a nem todos os programas terem suporte a JS, mas como a maioria irá interagir com esses
pdf no desktop ou mobile, é possivel que a maioria dos casos sejam capturados, teste deveram ser feitos.  

1) Subir servidor
para rodar o projeto 
uvicorn app.api:app --host 0.0.0.0 --port 8000 --reload --reload-dir /home/alessandro/Documentos/projetoLeadPdf
ou
uvicorn app.api2:app --host 0.0.0.0 --port 8000 --reload --reload-dir /home/alessandro/Documentos/projetoLeadPdf

2)testar urls que serão as urls inseridas no local onde se deseja rastrear o 
evento, o idela é que no local onde deseja monitorar as informações sejam add
via JS.

http://0.0.0.0:8000/qtd-form/1?nomeBotao=clique+aqui
 a url  url acima significa que 1 unidade será adicionada cada vez que essa urlfor chamada,nomeBotao é
 a variavel que receberá o nome "clique aqui" , que é o evento a ser monitorado.
 Por exemplo: ao add essa url "http://0.0.0.0:8000/qtd-form/1?nomeBotao=clique+aqui" no pdf
 toda vez que uma pessoa clicar no botão que contem esse atributoo a API irá incrementar uma unidade.