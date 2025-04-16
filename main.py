from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

def get_random_country():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        countries = response.json()
        country = random.choice(countries)
        return {
            "name": country.get("name", {}).get("common", "Неизвестно"),
            "flag": country.get("flags", {}).get("png", ""),
            "capital": country.get("capital", ["Не указано"])[0],
            "region": country.get("region", "Не указано"),
            "population": f"{country.get('population', 0):,}"
        }
    else:
        return {
            "name": "Ошибка",
            "flag": "",
            "capital": "-",
            "region": "-",
            "population": "-"
        }

@app.route('/')
def index():
    country = get_random_country()
    return render_template("index.html", country=country)

if __name__ == '__main__':
    app.run(debug=True)
