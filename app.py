from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Teste 123!'

@app.route('/contato')
def contato():
    x = "Maria"
    y = "maria@email.com"
    return render_template('contato.html', nome=x, email=y)

@app.route('/exemplo')
def exemplo():
    return render_template('exemplo.html')

@app.route('/exemplo2')
def exemplo2():
    return render_template('exemplo2.html')

@app.route('/perfil', defaults={'nome': 'fulano'})
@app.route('/perfil/<nome>')
def perfil(nome):
    return render_template('perfil.html', nome=nome)

@app.route('/semestre/<int:x>')
def semestre(x):
    y = x + 1
    return render_template('semestre.html', x=x, y=y)


@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1, n2):
    return str(n1+n2)

@app.route('/dados')
def dados():
    return render_template('dados.html')

@app.route('/recebedados', methods=['POST'])
def recebedados():
    #nome = request.args['nome']
    #telefone = request.args['telefone']
    nome = request.form['nome']
    telefone = request.form['telefone']
    estado = request.form['estado']
    #escolaridade = request.form['esc']
    escolaridade = request.form.getlist('esc')

    return f"{nome} - {telefone} - {estado} - {escolaridade}"

if __name__ == '__main__':
    app.run()