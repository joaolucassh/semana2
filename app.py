from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import redirect
from flask import url_for




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column('ID', db.Integer, primary_key=True)
    nome = db.Column('Nome', db.String(256))
    email = db.Column('Email', db.String(256))
    senha = db.Column('Senha', db.String(256))

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Vendas(db.Model):
    id = db.Column('ID', db.Intenger, primary_key=True)
    nome = db.Column('Nome', db.String(256))
    valor = db.Column('Valor', db.Intenger)
    quant = db.Column('quant', db.Intenger)
    descr = db.Column('descr', db.String(256))

    def __init__(self, id, nome, valor, quant, descr):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.quant = quant
        self.descr = descr

class Compras(db.Model):
    idcompra = dbColumn('ID', db.Intenger)
    nome = dbColumn('nome', db.String(256))
    quant = db.Column('quant', db.Intenger)
    valor = db.Column('Valor', db.Intenger)

    def __init__(self, idcompra, nome, quant, valor):
        self.idcompra = idcompra
        self.nome = nome
        self.quant = quant
        self.valor = valor

@app.errorhandler(404)
def erropagina(error):
    return render_template('erro.html')

@app.route("/")
def inicial():
    return render_template('inicial.html')

@app.route("/usuario")
def usuario():
    return render_template('usuario.html')

@app.route("/anuncios")
def anuncios():
    return render_template('anuncios.html')

@app.route("/usuario/cadastro")
def cadastro():
    return render_template('cadastro.html')

@app.route("/usuario/caduser", methods=['POST'])
def caduser():
    usuario = Usuario(request.form.get('name'), request.form.get('email'), request.form.get('senha'))
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for('usuario'))

@app.route("/usuario/perfil/<int:id>")
def perfiluser(id):
    usuario = Usuario.query.get(id)
    return usuario.nome

@app.route("/usuario/editar/<int:id>", methods=['GET','POST'])
def editaruser(id):
    usuario = Usuario.query.get(id)
    if request.method == 'POST':
        usuario.nome = request.form.get('nome')
        usuario.email = request.form.get('email')
        usuario.senha = request.form.get('senha')
        return redirect(url_for('usuario'))
    
    return usuario.nome

@app.route("/usuario/delete/<int:id>")
def deleteuser(id):
    usuario = Usuario.query.get(id) 
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('usuario'))




@app.route("/anuncios/cadastro")
def cadanuncio():
    return render_template('cadanuncio.html')

@app.route("/relatorio/vendas")
def vendas():
    return render_template('vendas.html')

@app.route("/relatorio/compras")
def compras():
    return render_template('compras.html')

@app.route("/anuncios/compra")
def comprado():
    return render_template('comprado.html')


if __name__ == 'myenv':
    print('myenv')
    db.create_all()




