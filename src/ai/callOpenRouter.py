import os
import requests
import json
import subprocess

###
def gerar_conteudo(system: str, user: str, model: str) -> str:
    prompt = f"{system}\n\n{user}"
    resultado = 


    return resultado.stdout.strip()
###

response = requests.post(
  url="https://openrouter.ai/api/v1/",  # Endpoint
  headers={
    "Authorization": f"Bearer {os.getenv("OPENROUTER_KEY")}", # Environment API key
  },
  data=json.dumps({
    "model": "", # Optional
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ]
  })
)
