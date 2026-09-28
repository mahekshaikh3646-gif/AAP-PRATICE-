import re 

text = """
for online makeup product , you can contact makeupstore@gmail.com. 
for product recommendation ans support,email makeuphelp@gmail.com
"""
email_pattern =r'[a-zA-Z9,_%+-]+@[a-zA-Z0-9,-]+\.[a-zA-Z]{2,}'

emails = re.findall(email_pattern,text) 

print("Email address found:")

for email in emails:
    print(email) 
