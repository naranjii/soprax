# sollax — Local AI Tweet Automation
---
<p align="left">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python" alt="Python"></a>
  <a href="https://www.selenium.dev/"><img src="https://img.shields.io/badge/Selenium-Automation-brightgreen?logo=selenium" alt="Selenium"></a>
  <a href="https://ollama.com/"><img src="https://img.shields.io/badge/Ollama-Required-green?logo=ollama" alt="Ollama"></a>
</p>

**Sollax** is a Python-based automation tool that leverages **Ollama** (a local LLM runtime) and **Selenium** to autonomously generate and publish tweets. Designed to run locally with full control, Sollax reads prompts from a JSON file, generates content using an LLM, and posts it on X (formerly Twitter) using a logged-in Chrome session.

> ⚠️ **Disclaimer**  
> This project is intended for **educational** and **portfolio** purposes only. It is a demonstration of local AI integration and browser automation. The author does not endorse or encourage automated behavior that violates platform terms of service or spam policies.

---

## ✨ Features

- 🔁 Fully automated tweet generation and posting
- 🧠 Runs local LLMs via [Ollama](https://ollama.com)
- 🖱️ Browser control using Selenium + ChromeDriver
- 📝 Configurable system/user prompts via JSON
- 🧩 Simple setup, no API keys or third-party dependencies

---

## 🛠️ Requirements

- Python 3.9+
- [Ollama](https://ollama.com/) (installed and running)
- Google Chrome browser
- ChromeDriver (version matching your Chrome)
- Virtual environment (optional but recommended)

---

## 📦 Installation

```bash
git clone https://github.com/naranjii/sollax.git
cd sollax
python -m venv venv
source venv/bin/activate    # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```
## Customize the behavior via the config.json file:
```json
{
  "system_prompt": "You are a clever, original, and concise content writer.",
  "user_prompt": "Post a short, smart tweet about AI trends in 2025.",
  "profile_path": "C:/Users/<your-user>/AppData/Local/Google/Chrome/User Data",
  "profile_name": "Default",
  "model": "llama3"
}
```
Ensure the Chrome user profile is already logged into X (Twitter).

Run Sollax
```bash
python sollax.py
```

## 🛡 Disclaimer (again)
- This repository is a proof-of-concept and is not intended to promote or facilitate abusive automation. Please respect the terms of service of any platform you interact with, including X (Twitter).

Use responsibly.

## To-do
- Add model to config.json
- Add schedule
- Enhance debug
- Add tweet log
- PT-BR Readme
