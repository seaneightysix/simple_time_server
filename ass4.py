import requests
import os
from bs4 import BeautifulSoup
from flask import Flask


app = Flask(__name__)

@app.route('/')
def get_time():
    response = requests.get("https://www.epochconverter.com/")
    soup = BeautifulSoup(response.content, "html.parser")
    time = soup.find("div", class_="ecclock")

    time = time.getText()

    return time

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)




