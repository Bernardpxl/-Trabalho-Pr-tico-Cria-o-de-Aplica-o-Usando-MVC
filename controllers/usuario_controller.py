from flask import Blueprint, request, jsonify
from services.usuario_service import UsuarioService
from services.chamado_service import ChamadoService

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/usuarios', methods=['GET'])
def listar():
    usuarios = UsuarioService.listar_todos()
    return jsonify([u.to_dict() for u in usuarios]), 200

@usuario_bp.route('/usuarios', methods=['POST'])
def criar():
    data = request.get_json() or {}
    try:
        novo = UsuarioService.criar_usuario(data)
        return jsonify(novo.to_dict()), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@usuario_bp.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar(id):
    data = request.get_json() or {}
    try:
        u = UsuarioService.atualizar_usuario(id, data)
        return jsonify(u.to_dict()), 200
    except KeyError as e:
        return jsonify({"erro": str(e).strip("'")}), 404
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@usuario_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar(id):
    try:
        UsuarioService.deletar_usuario(id)
        return jsonify({"msg": "Usuario deletado."}), 200
    except KeyError as e:
        return jsonify({"erro": str(e).strip("'")}), 404
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@usuario_bp.route('/usuarios/<int:id>/chamados', methods=['GET'])
def listar_chamados_usuario(id):
    try:
        chamados = ChamadoService.listar_por_usuario(id)
        return jsonify([c.to_dict() for c in chamados]), 200
    except KeyError as e:
        return jsonify({"erro": str(e).strip("'")}), 404