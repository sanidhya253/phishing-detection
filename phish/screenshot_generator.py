from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from PIL import Image, ImageDraw, ImageFont
import os

def generate_screenshot(url):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
          Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
          });
        """
    })

    try:
        driver.set_window_size(1200, 800)
        driver.get(url)
        time.sleep(3)

        if "facebook.com" in url:
            try:
                login_box = driver.find_element(By.ID, "loginform")
                driver.execute_script("arguments[0].style.border='3px solid red'", login_box)
            except:
                 pass  # fail silently if not found

        screenshot_path = 'static/screenshot.png'
        driver.save_screenshot(screenshot_path)

        image = Image.open(screenshot_path)
        draw = ImageDraw.Draw(image)

        final_url = driver.current_url
        font = ImageFont.load_default()

        # Draw red box only around URL area at top of the image
        draw.rectangle([0, 0, 1200, 20], outline="red", width=4)
        draw.rectangle([0, 0, 1200, 20], fill="white")
        draw.text((10, 2), final_url, fill="black", font=font)

        image.save(screenshot_path)

    except Exception as e:
        print("Screenshot error:", e)
        screenshot_path = None
    finally:
        driver.quit()

    return screenshot_path