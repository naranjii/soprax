from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def postar_tweet(text, chrome_profile_path):
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument(
        f"--user-data-dir={chrome_profile_path}"
    )  # full path to the profile directory
    # options.add_argument("--headless=new")  # run in background if desired
    options.add_argument("--disable-gpu")
    print("[DEBUG] Starting Chrome driver...")
    try:
        driver = webdriver.Chrome(options=options)
    except Exception as e:
        print(f"[ERROR] Failed to start ChromeDriver: {e}")
        return
    try:
        driver.get("https://x.com/compose/tweet")
        time.sleep(5)
        print("[DEBUG] Looking for tweet text box...")
        try:
            box = driver.find_element(By.XPATH, '//div[@aria-label="Post text"]')
        except Exception as e:
            print(f"[ERROR] Tweet text box not found: {e}")
            
            return
        # Remove surrounding double quotes if present
        if isinstance(text, str) and text.startswith('"') and text.endswith('"'):
            text = text[1:-1]
        box.send_keys(text)
        time.sleep(2)
        print("[DEBUG] Looking for post button...")
        try:
            post = driver.find_element(By.XPATH, "//button[@data-testid='tweetButton']")
        except Exception as e:
            print(f"[ERROR] Post button not found: {e}")
            
            return
        print("[DEBUG] 🐦 Sollax tweets... ")
        driver.execute_script("arguments[0].click();", post)
        time.sleep(5)
    except Exception as e:
        print(f"[ERROR] Unexpected error while sending tweet: {e}")
    finally:
        print("[DEBUG] Closing Chrome driver...")
        
