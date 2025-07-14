from flask import Flask, request, render_template, send_file
import os
from phishing_check import is_phishing_url, get_explanation
from screenshot_generator import generate_screenshot

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    url = request.form.get('url')
    selected_service = request.form.get('service')
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"URL received: {url}\n")
    result, real_url = is_phishing_url(url)
    explanation = get_explanation(url, result, real_url,selected_service)
    screenshot_path = generate_screenshot(real_url)

    return render_template('result.html', 
                           url=url,
                           result=result,
                           explanation=explanation,
                           screenshot_path=screenshot_path)

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    app.run(debug=True)