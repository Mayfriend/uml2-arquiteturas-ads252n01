from flask import Blueprint, request, jsonify
from db import conectar

matricula_bp = Blueprint("matricula", _name_)


def resposta(status, mensagem, codigo=200):
    return jsonify({"status": status, "mensagem": mensagem}), codigo


@matricula_bp.route("/matricula", methods=["POST"])
def matricular():
    dados = request.get_json(silent=True) or {}
    aluno_id = dados.get("aluno_id")
    disciplina_id = dados.get("disciplina_id")
    if not aluno_id or not disciplina_id:
        return resposta("erro", "Informe aluno_id e disciplina_id.", 400)
    conn = conectar()
    try:
        return efetivar_matricula(conn, aluno_id, disciplina_id)
    finally:
        conn.close()

def validar_matricula(cur, aluno_id, disciplina_id):
    """Devolve uma mensagem de erro, ou None se estiver tudo certo."""
    cur.execute("SELECT 1 FROM alunos WHERE id = %s", (aluno_id,))
    if cur.fetchone() is None:
        return "Aluno não encontrado."

    cur.execute("SELECT vagas FROM disciplinas WHERE id = %s", (disciplina_id,))
    linha = cur.fetchone()
    if linha is None:
        return "Disciplina não encontrada."
    if linha[0] <= 0:
        return "Não há vagas nesta disciplina."

    cur.execute(
        "SELECT 1 FROM matriculas WHERE aluno_id = %s AND disciplina_id = %s",
        (aluno_id, disciplina_id),
    )
    if cur.fetchone() is not None:
        return "Você já está matriculado nesta disciplina."
    return None
