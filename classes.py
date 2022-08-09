import requests
from datetime import datetime

class CoinGeckoAPI:
    def __init__(self,url_base:str):
        self.url_base=url_base

    def ping(self)->bool:
        url=f'{self.url_base}/ping'
        return requests.get(url).status_code==200

    def consulta_preco(self,id_moeda):
        url=f'{self.url_base}/simple/price?ids={id_moeda}&vs_currencies=BRL&include_last_updated_at=true'
        resposta=requests.get(url)
        if resposta.status_code==200:
            dados_moeda = resposta.json().get(id_moeda, None)
            preco = dados_moeda.get('brl', None)
            atualizado_em = dados_moeda.get('last_updated_at', None)
            data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')
        else:








class TelegramBot:
    pass