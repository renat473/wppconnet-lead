from asyncio import sleep
import requests
import json
import time


with open('lead.txt') as f:
    content = f.readlines()

    for linhas in content:

        contatos = linhas.rstrip('\n')
        #print(contatos)

        url = "http://localhost:21465/api/devopsdays/send-message"

        payload = json.dumps({
        "phone": ""+contatos+"",
        "message": "texto para ser enviado",
        "isGroup": False
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer $2b$10$StQ3Fu7c6htx6TCRTzk1FOtQ7i.Wh5EJASzcO1lH_V.A6LvSlSLqC'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        resposta = response.json()
        print ("Mensagem enviada para , " + contatos + resposta['status'])
        time.sleep(15)
