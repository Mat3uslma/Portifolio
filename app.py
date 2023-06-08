from flask import Flask

app = Flask (__name__)
@app.route("/")
def pagina_inicial():
    return "Teste"
@app.route("/blog")
def blog ():
    return "Blog"
@app.route("/contato")
def contato():
    return "Contato"

app.run()