import os
import requests
import json


def gerar_conteudo(systemPrompt: str, userPrompt: str, model: str) -> str:
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",  # Correct endpoint
        headers={
            "Authorization": f"Bearer {os.getenv('OPENROUTER_KEY')}",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "model": model,
            "messages": [
                {"role": "system", "content": systemPrompt},
                {"role": "user", "content": userPrompt}
            ]
        })
    )
    if response.status_code != 200:
        raise Exception(f"OpenRouter API error: {response.status_code} {response.text}")
    data = response.json()
    # Extract the content from the response
    return data["choices"][0]["message"]["content"]