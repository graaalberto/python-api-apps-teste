from flask import Flask, render_template, request, redirect, session
from db import get_db, init_db

app = Flask(__name__)
app.secret_key = "segredo"

# Inicializa tabelas
init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastro", methods=["GET","POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        telefone = request.form["telefone"]
        documento = request.form["documento"]
        endereco = request.form["endereco"]

        db = get_db()
        db.execute("INSERT INTO alunos (nome,email,senha,telefone,documento,endereco) VALUES (?,?,?,?,?,?)",
                   (nome,email,senha,telefone,documento,endereco))
        db.commit()
        db.close()
        return redirect("/login")
    return render_template("cadastro.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        db = get_db()
        aluno = db.execute("SELECT * FROM alunos WHERE email=? AND senha=?",(email,senha)).fetchone()
        db.close()

        if aluno:
            session["aluno_id"] = aluno["id"]
            return redirect("/notas")
        else:
            return "Email ou senha inválidos."
    return render_template("login.html")

@app.route("/notas", methods=["GET","POST"])
def notas():
    if "aluno_id" not in session:
        return redirect("/login")

    db = get_db()
    if request.method == "POST":
        disciplina = request.form["disciplina"]
        valor = request.form["valor"]
        semestre = request.form["semestre"]
        observacao = request.form["observacao"]

        db.execute("INSERT INTO notas (aluno_id,disciplina,valor,semestre,observacao) VALUES (?,?,?,?,?)",
                   (session["aluno_id"],disciplina,valor,semestre,observacao))
        db.commit()

    notas = db.execute("SELECT * FROM notas WHERE aluno_id=?",(session["aluno_id"],)).fetchall()
    db.close()
    return render_template("notas.html", notas=notas)

if __name__ == "__main__":
    app.run(debug=True)
