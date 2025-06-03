from flask import Flask, render_template, request, redirect, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'chave_secreta_segura'  # Necessário para usar flash()

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_escola"
)
cursor = conexao.cursor(dictionary=True)

@app.route('/')
def index():
    cursor.execute("SELECT a.id, a.nome, a.matricula, t.nome AS turma, a.id_tb_turma FROM tb_aluno a LEFT JOIN tb_turma t ON a.id_tb_turma = t.id")
    alunos = cursor.fetchall()

    cursor.execute("SELECT * FROM tb_turma")
    turmas = cursor.fetchall()

    return render_template('index.html', alunos=alunos, turmas=turmas)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    matricula = request.form['matricula']
    id_tb_turma = request.form['id_tb_turma']

    try:
        cursor.execute("INSERT INTO tb_aluno (nome, matricula, id_tb_turma) VALUES (%s, %s, %s)", 
                       (nome, matricula, id_tb_turma))
        conexao.commit()
        flash('Aluno cadastrado com sucesso!', 'success')
    except mysql.connector.Error as err:
        flash(f'Erro ao cadastrar: {err}', 'danger')
    return redirect('/')

@app.route('/excluir/<int:id>')
def excluir(id):
    cursor.execute("DELETE FROM tb_aluno WHERE id = %s", (id,))
    conexao.commit()
    flash('Aluno excluído com sucesso!', 'warning')
    return redirect('/')

@app.route('/editar/<int:id>', methods=['POST'])
def editar(id):
    nome = request.form['nome']
    matricula = request.form['matricula']
    id_tb_turma = request.form['id_tb_turma']

    try:
        cursor.execute("UPDATE tb_aluno SET nome = %s, matricula = %s, id_tb_turma = %s WHERE id = %s",
                       (nome, matricula, id_tb_turma, id))
        conexao.commit()
        flash('Aluno atualizado com sucesso!', 'info')
    except mysql.connector.Error as err:
        flash(f'Erro ao editar: {err}', 'danger')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
