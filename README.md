🛡️ Phishing URL Detection System
This project is a web-based tool that helps detect phishing login pages. Users can select the intended login service (e.g., Google or Facebook) and paste the URL they received. The system analyzes the page in a headless browser, takes a screenshot, and gives a verdict on whether it is likely safe, legitimate, or phishing.

🧰 Getting Started
📦 Clone the repository
git clone https://github.com/sanidhya253/phishing-detection.git
cd phishing-detection

🚀 Features
🔍 User selects expected login type (Google/Facebook)
🌐 URL is visited and analyzed in a headless Chrome browser
🔐 Password fields are detected and evaluated
🎯 Comparison of actual vs. expected domain
📸 Screenshot is taken with red highlight on suspicious elements
💬 Clear explanations of why the page is safe or suspicious

🧪 How It Works
1.User Input:
Choose login service (Google/Facebook)
Paste suspected URL

2.Analysis:
The tool opens the URL in an automated browser
Checks if the domain matches the selected service
Checks for password fields
Takes a screenshot and highlights login elements

3.Output:
Verdict: Verified Legit / Likely Phishing / Likely Safe
Explanation of the verdict
Screenshot proof

🛠️ Requirements
Install the following Python packages:
pip install flask selenium pillow
You’ll also need Google Chrome and ChromeDriver installed and added to your system path.

