from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])
    imc = peso / (altura ** 2)

    # Determina a classificação do IMC
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        classificacao = "Peso normal"
    elif 25 <= imc < 29.9:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    return render_template('result.html', resultado=imc, tipo=classificacao, peso=peso, altura=altura)

if __name__ == "__main__":
    app.run(debug=True)
