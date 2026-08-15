from flask import Blueprint, request, jsonify
from services.chamado_service import ChamadoService

chamado_bp = Blueprint('chamado_bp', __name__)

@chamado_bp.route('/chamados', methods=['GET'])
def listar():
    chamados = ChamadoService.listar_todos()
    return jsonify([c.to_dict() for c in chamados]), 200

@chamado_bp.route('/chamados', methods=['POST'])
def criar():
    data = request.get_json() or {}
    try:
        novo = ChamadoService.criar_chamado(data)
        return jsonify(novo.to_dict()), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@chamado_bp.route('/chamados/<int:id>', methods=['PUT'])
def atualizar(id):
    data = request.get_json() or {}
    try:
        c = ChamadoService.atualizar_chamado(id, data)
        return jsonify(c.to_dict()), 200
    except KeyError as e:
        return jsonify({"erro": str(e).strip("'")}), 404
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@chamado_bp.route('/chamados/<int:id>', methods=['DELETE'])
def deletar(id):
    try:
        ChamadoService.deletar_chamado(id)
        return jsonify({"msg": "Chamado deletado."}), 200
    except KeyError as e:
        return jsonify({"erro": str(e).strip("'")}), 404

@chamado_bp.route('/chamados/<int:id>/iniciar', methods=['PATCH'])
def iniciar(id):
    try:
        c = ChamadoService.iniciar_atendimento(id)
        return jsonify(c.to_dict()), 200
    except KeyError as e:
        return jsonify({"erro": str(e).strip("'")}), 404
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@chamado_bp.route('/chamados/<int:id>/encerrar', methods=['PATCH'])
def encerrar(id):
    try:
        c = ChamadoService.encerrar_chamado(id)
        return jsonify(c.to_dict()), 200
    except KeyError as e:
        return jsonify({"erro": str(e).strip("'")}), 404
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@chamado_bp.route('/chamados/abertos', methods=['GET'])
def listar_abertos():
    chamados = ChamadoService.listar_abertos()
    return jsonify([c.to_dict() for c in chamados]), 200

@chamado_bp.route('/chamados/prioridade/alta', methods=['GET'])
def listar_prioridade_alta():
    chamados = ChamadoService.listar_alta_prioridade()
    return jsonify([c.to_dict() for c in chamados]), 200

@chamado_bp.route('/estatisticas', methods=['GET'])
def estatisticas():
    dados = ChamadoService.obter_estatisticas()
    return jsonify(dados), 200