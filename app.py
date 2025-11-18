from flask import Flask, render_template, request
from utils import db
import os
from models import Usuario
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db_usuario = os.getenv('DB_USERNAME')
db_senha = os.getenv('DB_PASSWORD')
db_mydb = os.getenv('DB_DATABASE')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

conexao = f"mysql+pymysql://{db_usuario}:{db_senha}@{db_host}:{db_port}/{db_mydb}"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verificarlogin', methods=['POST'])
def verificarlogin():
    login = request.form['login']
    senha = request.form['senha']
    if login == 'admin' and senha == '12345':
        return 'Olá admin'
    else:
        return 'Você não tem permissão de visualizar essa página'

@app.route('/verificaridade/<int:idade>')
def verificaridade(idade):
    return render_template('verificaridade.html', idade=idade)

@app.route('/usuario/<nome>')
def usuario(nome):
    return render_template('usuario.html', nome=nome)

@app.route('/produtos/<int:qtd>')
def produtos(qtd):
    return render_template('produtos.html', qtd=qtd)

@app.route('/lista')
def lista():
    return render_template('lista.html')

@app.route('/compras', methods=['POST'])
def compras():
    #itens = ['Arroz', 'Feijão', 'Macarrão','Açúcar', 'Farinha', 'Tomate', 'Cebola', 'Alho']
    itens = request.form.getlist('item')
    return render_template('compras.html', itens=itens)

if __name__ == '__main__':
    app.run()