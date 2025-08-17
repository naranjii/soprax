from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time

with open("../../config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

def followbot(addFollowCount, chrome_profile_path):
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument(f"--user-data-dir={chrome_profile_path}")  # full path to the profile directory
    # options.add_argument("--headless=new")  # run in background if desired
    options.add_argument("--disable-gpu")
    print("[DEBUG] Starting Chrome driver...")
    try:
        driver = webdriver.Chrome(options=options)
    except Exception as e:
        print(f"[ERROR] Failed to start ChromeDriver: {e}")
        return
    try:
        driver.get("https://x.com/following")
        time.sleep(5)
        print("[DEBUG] Looking for first following user ...")
        try:
            following_div = driver.find_element(By.XPATH, '//div[@aria-label="Timeline: Following"]')
            first_button = following_div.find_element(By.XPATH, ".//button")
            driver.execute_script("arguments[0].click();", first_button)
        except Exception as e:
            print(f"[ERROR] Following div or button not found {e}")
            driver.quit()
            return
        '''
        print("[DEBUG] First user found")
        print("[DEBUG] Looking for 1st user followers...")
        try:
            post = driver.find_element(By.XPATH, "//button[@data-testid='tweetButton']")
        except Exception as e:
            print(f"[ERROR] Post button not found: {e}")
            driver.quit()
            return
        print("[DEBUG] 🐦 Sollax tweets... ")
        driver.execute_script("arguments[0].click();", post)
        time.sleep(5)
        '''
    except Exception as e:
        print(f"[ERROR] Unexpected error while sending tweet: {e}")
    finally:
        print("[DEBUG] Closing Chrome driver...")
        driver.quit()

followbot(100, config["chrome_profile_path"])