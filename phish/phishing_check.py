from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from urllib.parse import urlparse

def is_phishing_url(url):
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
        final_url = driver.current_url
        parsed = urlparse(final_url)
        domain = parsed.netloc

        has_password = driver.find_elements(By.XPATH, "//input[@type='password']")

        if domain == "accounts.google.com":
            return ("Verified Legit", final_url)
        elif domain == "www.facebook.com" or domain == "facebook.com":
            return ("Verified Legit", final_url)
        elif has_password:
            return ("Likely Phishing", final_url)
        else:
            return ("Likely Safe", final_url)

    except Exception as e:
        print("Error while checking phishing status:", e)
        return ("Unknown", url)
    finally:
        driver.quit()

def get_explanation(input_url, verdict, real_url, selected_service):
    from urllib.parse import urlparse
    reasons = []
    parsed = urlparse(real_url)
    domain = parsed.netloc

    if verdict == "Verified Legit":
        if domain == "accounts.google.com":
            reasons.append(f"The domain '{domain}' is a verified Google login page.")
        elif domain == "www.facebook.com" or domain == "facebook.com":
            reasons.append(f"The domain '{domain}' is a verified Facebook login page.")
    elif verdict == "Likely Phishing":
        if selected_service == "google":
            reasons.append(f"This page contains a password input and seems to imitate Google, but it is not from Google's domain.")
        elif selected_service == "facebook":
            reasons.append(f"This page contains a password input and seems to imitate Facebook, but it is not from Facebook's domain.")
        else:
            reasons.append(f"This page contains a password input, but the domain '{domain}' is not trusted.")
    elif verdict == "Likely Safe":
        reasons.append(f"The page does not contain any login form.")
    else:
        reasons.append("Unable to determine status due to browser or connection error.")

    return reasons if reasons else ["No explanation available."]
