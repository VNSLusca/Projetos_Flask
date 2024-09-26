import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/IMC", methods=['POST'])
def descobrir_imc():
    altura = float(request.form["altura"])
    peso = float(request.form["peso"])

    if altura <= 0:
        raise ValueError("Altura deve ser maior que zero.")

    imc = round(peso/(altura*altura), 1)
    

    if imc < 16.9:
        status = "Muito Abaixo do Peso"
    elif imc <= 18.4:
        status = "Abaixo do Peso"
    elif imc <=24.9:
        status = "PESO NORMAL"
    elif imc <=29.9:
        status = "SOBREPESO"
    elif imc <=34.9:
        status = "OBESIDADE I"
    elif imc <=40:
        status = "OBESIDADE II"
    elif imc > 40:
        status = "OBESIDADE III"

    caminho_arquivo = 'models/notas.txt'

      # Verificar se o diretório 'models' existe, se não, criar
    if not os.path.exists('models'):
        os.makedirs('models')

    # Verificar se o arquivo 'notas.txt' existe, se não, criar
    if not os.path.isfile(caminho_arquivo):
        with open(caminho_arquivo, 'w') as arquivo:
            pass  # Cria o arquivo vazio

    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(f"{altura};{peso};{imc}; {status}\n")

    return render_template("index.html", imc=imc, status=status)

app.run(host='127.0.0.1', port=80, debug=True)