class StoreArtefatosClicados():
    def __init__(self, nomeBotao="", qtd_clique=0):
        self.qtd_clique:int = qtd_clique
        self.nomeBotao:str = nomeBotao

    def __str__(self) -> str:
        return self.nomeBotao
    
    def __repr__(self) -> str:
        return self.nomeBotao