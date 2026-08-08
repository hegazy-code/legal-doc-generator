from flask import Flask, request, render_template_string

app = Flask(__name__)

form_page = """
<h1>Legal Document Generator</h1>
<form method="POST" action="/generate">
  Business Name: <input type="text" name="business_name"><br><br>
  Website URL: <input type="text" name="website_url"><br><br>
  Country: <input type="text" name="country"><br><br>
  Do you collect emails?
  <select name="collects_email">
    <option value="yes">Yes</option>
    <option value="no">No</option>
  </select><br><br>
  Does your site use cookies?
  <select name="uses_cookies">
    <option value="yes">Yes</option>
    <option value="no">No</option>
  </select><br><br>
  <input type="submit" value="Generate Documents">
</form>
"""

@app.route("/")
def home():
    return form_page

@app.route("/generate", methods=["POST"])
def generate():
    business_name = request.form["business_name"].strip().title()
    website_url = request.form["website_url"].strip()
    country = request.form["country"].strip().title()
    collects_email = request.form["collects_email"]
    uses_cookies = request.form["uses_cookies"]

    policy = f"""PRIVACY POLICY

Last updated: 2026

{business_name} ("we", "us", or "our") operates the website {website_url}.

This page informs you of our policies regarding the collection, use, and disclosure of personal data.

1. Information We Collect
"""
    if collects_email == "yes":
        policy += "\nWe collect your email address when you interact with our website (e.g. signing up, contacting us).\n"
    if uses_cookies == "yes":
        policy += "\nWe use cookies to improve your experience on our website.\n"

    policy += f"""
2. Governing Law
This policy is governed by the laws of {country}.

3. Contact Us
If you have questions about this Privacy Policy, contact us through {website_url}.
"""

    terms = f"""TERMS AND CONDITIONS

Last updated: 2026

Welcome to {website_url}, operated by {business_name}.

By accessing this website, you agree to be bound by these Terms and Conditions.

1. Use of the Website
You agree to use this website only for lawful purposes and in accordance with these Terms.

2. Intellectual Property
All content on {website_url}, including text, graphics, and logos, is the property of {business_name} unless otherwise stated.

3. Limitation of Liability
{business_name} is not liable for any damages resulting from the use of this website.

4. Governing Law
These Terms are governed by the laws of {country}.

5. Contact Us
Questions about these Terms can be sent through {website_url}.
"""

    return f"<h2>Privacy Policy</h2><pre>{policy}</pre><h2>Terms and Conditions</h2><pre>{terms}</pre>"

if __name__ == "__main__":
    app.run(debug=True)