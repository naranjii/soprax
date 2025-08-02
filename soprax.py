import json
import os
from src.ai.callOpenRouter import gerar_conteudo
from src.selenium.tweet_sender import postar_tweet


with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
print("🟢 config.json loaded")
# Gera o tweet
tweet = gerar_conteudo(
    system=config["system_prompt"],
    user=config["user_prompt"],
    model=config["model"]
)
print("🐦 Soprax says:\n", tweet)
log_dir = "data"
log_file = os.path.join(log_dir, "log.txt")
os.makedirs(log_dir, exist_ok=True)
with open(log_file, "a", encoding="utf-8") as log:
    log.write(tweet + "\n\n")
# Posta o tweet
postar_tweet(tweet, config["chrome_profile_path"])
print("🔥 Tweet posted ")
