business_name = input("Enter your business name: ").strip().title()
website_url = input("Enter your website URL: ")
country = input("Enter your country: ").strip().title()
collects_email = input("Do you collect emails? (yes/no): ")
uses_cookies = input("Does your site use cookies? (yes/no): ")

policy = f"""
PRIVACY POLICY

Last updated: 2026

{business_name} ("we", "us", or "our") operates the website {website_url}.

This page informs you of our policies regarding the collection, use, and disclosure of personal data.

1. Information We Collect
"""

if collects_email.lower() == "yes":
    policy += "\nWe collect your email address when you interact with our website (e.g. signing up, contacting us).\n"

if uses_cookies.lower() == "yes":
    policy += "\nWe use cookies to improve your experience on our website.\n"

policy += f"""
2. Governing Law
This policy is governed by the laws of {country}.

3. Contact Us
If you have questions about this Privacy Policy, contact us through {website_url}.
"""

with open("privacy_policy.txt", "w") as f:
    f.write(policy)

print("Privacy policy generated! Check privacy_policy.txt")

terms = f"""
TERMS AND CONDITIONS

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

with open("terms_and_conditions.txt", "w") as f:
    f.write(terms)

print("Terms and conditions generated! Check terms_and_conditions.txt")