from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GIPHY_API_KEY = "CErHsZdiLFBB7GpphjQrAv5OT2kHpkM1"

@app.route("/", methods=["GET", "POST"])
def index():
    gifs = []
    if request.method == "POST":
        termo = request.form["termo"]
        url = f"https://api.giphy.com/v1/gifs/search"
        params = {
            "api_key": GIPHY_API_KEY, #Chave da api
            "q": termo, #Consulta(pesquisar)
            "limit": 500, #Quantidade de gifs a ser exibido
            "rating": "g" #Conteúdo(livre para todos os públicos)
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            gifs = [item["images"]["downsized_medium"]["url"] for item in data["data"]]
        else:
            print("Erro ao buscar GIFs:", response.status_code)
    return render_template("index.html", gifs=gifs)

if __name__ == "__main__":
    app.run(debug=True)
