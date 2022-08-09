import locale
from datetime import datetime
from time import sleep

import requests
import telegram


#configuração da localização de escrita
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#atualizacoes=bot.get_updates()
# necessita do id do usuario que mandou a menssagem

# pass


#url base
URL_BASE = 'https://api.coingecko.com/api/v3'

ENDPOINT_PING = f'{URL_BASE}/ping'
ENDPOINT_PRECOS = f'{URL_BASE}/simple/price'
#configuração do bot do telegram
bot=telegram.Bot(token='5530120844:AAFp8d6wYYR_D2YWnLqsU02Afu62nFv21sI')
while True:
    resposta = requests.get(ENDPOINT_PING)
#configuração da resposta

    if resposta.status_code == 200:
     #tratamento do json obtido pela api do CoinGecko
        url = f'{ENDPOINT_PRECOS}?ids=ethereum&vs_currencies=brl&include_last_updated_at=true'
        resposta = requests.get(url).json()
        dados = resposta.get('ethereum', None)
        preco = dados.get('brl', None)
        atualizado = dados.get('last_updated_at')
        data_hora = datetime.fromtimestamp(atualizado).strftime(' %A %x %X')
        mensagen =None
        if preco<9000:
            mensagen=f'*Ethereum*:\n\t*Preço*  {preco}\n\t*Atualizado em :*{data_hora}\n\t*Valor em Baixa Aconselho a comprar *'

        elif preco>9000 and preco<10000:
            mensagen = f'*Ethereum*:\n\t*Preço*  {preco}\n\t*Atualizado em :*{data_hora}\n\t*Valor em Alta-Média talvez deva vender *'

        elif preco>10000:
            mensagen = f'*Ethereum*:\n\t*Preço*  {preco}\n\t*Atualizado em :*{data_hora}\n\t*Valor em Alta Aconselho a Venda total *'


        if mensagen:
            bot.send_message(text=mensagen, chat_id=1647892817, parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        mensagen = f'*API OFFLINE TENTE NOVAMENTE MAIS TARDE*'
        bot.send_message(text=mensagen, chat_id=1647892817, parse_mode=telegram.ParseMode.MARKDOWN)

    sleep(15)
pass
