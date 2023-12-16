from flask import Flask, render_template
import requests

app = Flask(__name__)


def obtener_datos():
    URL = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
    json = requests.get(URL).json()
    datos = []

    for index, emoji in enumerate((""',"'"')):
        compra = json[index]["casa"]["compra"][:-1]
        venta = json[index]["casa"]["venta"][:-1]
        datos.append({"emoji": emoji, "compra": compra, "venta": venta})

    return datos


@app.route("/")
def index():
    datos = obtener_datos()
    return render_template("index.html", datos=datos)


if __name__ == "__main__":
    app.run(debug=True)
