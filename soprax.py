import json
import os
from src.ai.callOpenRouter import gerar_conteudo
from src.selenium.tweet_sender import postar_tweet
print("🟡 Starting Soprax.py ...")
print("🟡 Loading config.json ...")

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

print("🟢 config.json loaded ...")
print("🟡 Requesting OpenRouter ...")

tweet = gerar_conteudo(
    systemPrompt=config["system_prompt"], userPrompt=config["user_prompt"], model=config["model"]
)

print("🟢 Soprax 🤖💬:\n", tweet)
print("🟡 Adding tweet to log ...")

log_dir = "data"
log_file = os.path.join(log_dir, "log.txt")
os.makedirs(log_dir, exist_ok=True)
with open(log_file, "a", encoding="utf-8") as log:
    log.write(tweet + "\n\n")
    
print("🟢 Tweet logged to ~/soprax/data/log.txt ...")
print("🟡 Running webdriver profile and posting tweet ...")

postar_tweet(tweet, config["chrome_profile_path"])

print("✅ Tweet succesfully posted! 🤖👍")
