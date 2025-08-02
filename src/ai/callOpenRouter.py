import os
import requests
import json
###


def pedir_conteudo(systemPrompt: str, userPrompt: str, model: str) -> str:
  requests.post(
    url="https://openrouter.ai/api/v1/",  # Endpoint
    headers={
    "Authorization": f"Bearer {os.getenv("OPENROUTER_KEY")}", # Environment API key
  },
  data=json.dumps({
    "model": f"{model}",
    "messages": [
      {
        "role": "system",
        "content": f"{systemPrompt}"
      },
      {
        "role":"user",
        "content": f"{userPrompt}"
      }
    ]
  })
)
def gerar_conteudo()