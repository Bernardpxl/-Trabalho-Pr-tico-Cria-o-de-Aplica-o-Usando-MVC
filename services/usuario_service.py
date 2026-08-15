from repositories.usuario_repository import UsuarioRepository
from repositories.chamado_repository import ChamadoRepository
from models.usuario import Usuario

class UsuarioService:
    @staticmethod
    def listar_todos():
        return UsuarioRepository.get_all()

    @staticmethod
    def buscar_por_id(id):
        return UsuarioRepository.get_by_id(id)

    @staticmethod
    def criar_usuario(data):
        nome = data.get('nome')
        email = data.get('email')
        setor = data.get('setor')

        if not nome or not email:
            raise ValueError("Nome e email sao obrigatorios.")

        if UsuarioRepository.get_by_email(email):
            raise ValueError("Email ja cadastrado.")

        novo = Usuario(nome=nome, email=email, setor=setor)
        return UsuarioRepository.create(novo)

    @staticmethod
    def atualizar_usuario(id, data):
        user = UsuarioRepository.get_by_id(id)
        if not user:
            raise KeyError("Usuario nao encontrado.")

        email = data.get('email', user.email)
        if email != user.email:
            if UsuarioRepository.get_by_email(email):
                raise ValueError("Email ja em uso por outro usuario.")

        user.nome = data.get('nome', user.nome)
        user.email = email
        user.setor = data.get('setor', user.setor)

        return UsuarioRepository.update(user)

    @staticmethod
    def deletar_usuario(id):
        user = UsuarioRepository.get_by_id(id)
        if not user:
            raise KeyError("Usuario nao encontrado.")

        chamados = ChamadoRepository.get_by_usuario_id(id)
        if chamados:
            raise ValueError("Nao pode deletar usuario com chamados.")

        UsuarioRepository.delete(user)