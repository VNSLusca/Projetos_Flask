from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/validar_notas", methods=['POST'])
def validar_notas():
    nome_aluno = request.form["nome_aluno"]
    nota_1 = float(request.form["nota_1"])
    nota_2 = float(request.form["nota_2"])
    nota_3 = float(request.form["nota_3"])
    
    media = (nota_1 + nota_2 + nota_3) / 3 

    if media >= 7:
        status = "Aprovado"
    elif media >= 3:
        status = "Recuperação"
    else:
        status = "Reprovado"

    caminho_arquivo = 'models/notas.txt'

    # Salvando os dados no arquivo
    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(f"{nome_aluno};{nota_1};{nota_2};{nota_3};{media};{status}\n")

    return redirect("/")

@app.route("/consulta")
def consultar_notas():
    notas = []
    caminho_arquivo = 'models/notas.txt'

    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            item = linha.strip().split(';')
            # Verificar se a linha tem exatamente 5 itens (nome, valor, quantidade, nota e média)
            if len(item) == 6:
                notas.append({
                    'nome': item[0],
                    'nota_2': item[1],
                    'nota_3': item[2],
                    'nota_1': item[3],
                    'media':  item[4],
                    'status': item[5],
                })  

    return render_template("verificar_nota.html", prod=notas)

app.run(host='127.0.0.1', port=80, debug=True)