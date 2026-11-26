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
