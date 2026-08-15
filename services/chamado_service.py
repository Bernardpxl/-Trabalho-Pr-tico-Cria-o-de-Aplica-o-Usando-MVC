from repositories.chamado_repository import ChamadoRepository
from repositories.usuario_repository import UsuarioRepository
from models.chamado import Chamado

class ChamadoService:
    @staticmethod
    def listar_todos():
        return ChamadoRepository.get_all()

    @staticmethod
    def buscar_por_id(id):
        return ChamadoRepository.get_by_id(id)

    @staticmethod
    def listar_por_usuario(usuario_id):
        if not UsuarioRepository.get_by_id(usuario_id):
            raise KeyError("Usuario nao existe.")
        return ChamadoRepository.get_by_usuario_id(usuario_id)

    @staticmethod
    def listar_abertos():
        return ChamadoRepository.get_by_status("Aberto")

    @staticmethod
    def listar_alta_prioridade():
        return ChamadoRepository.get_by_prioridade("Alta")

    @staticmethod
    def criar_chamado(data):
        titulo = data.get('titulo')
        descricao = data.get('descricao')
        prioridade = data.get('prioridade')
        usuario_id = data.get('usuario_id')
        tecnico = data.get('tecnico')

        if not titulo or len(titulo) < 5:
            raise ValueError("Titulo deve ter no minimo 5 caracteres.")
        
        if not descricao or len(descricao) < 10:
            raise ValueError("Descricao deve ter no minimo 10 caracteres.")

        if not usuario_id or not UsuarioRepository.get_by_id(usuario_id):
            raise ValueError("Usuario informado nao existe.")

        if prioridade not in ['Baixa', 'M�dia', 'Alta']:
            raise ValueError("Prioridade invalida.")

        if prioridade == 'Alta':
            qtd = ChamadoRepository.count_altos_abertos(usuario_id)
            if qtd >= 5:
                raise ValueError("Usuario ja possui 5 chamados de alta prioridade abertos.")

        novo = Chamado(
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade,
            status='Aberto',
            tecnico=tecnico,
            usuario_id=usuario_id
        )

        return ChamadoRepository.create(novo)

    @staticmethod
    def atualizar_chamado(id, data):
        c = ChamadoRepository.get_by_id(id)
        if not c:
            raise KeyError("Chamado nao encontrado.")

        titulo = data.get('titulo', c.titulo)
        descricao = data.get('descricao', c.descricao)
        prioridade = data.get('prioridade', c.prioridade)

        if len(titulo) < 5:
            raise ValueError("Titulo muito curto.")
        if len(descricao) < 10:
            raise ValueError("Descricao muito curta.")
        if prioridade not in ['Baixa', 'M�dia', 'Alta']:
            raise ValueError("Prioridade invalida.")

        c.titulo = titulo
        c.descricao = descricao
        c.prioridade = prioridade
        c.tecnico = data.get('tecnico', c.tecnico)

        return ChamadoRepository.update(c)

    @staticmethod
    def deletar_chamado(id):
        c = ChamadoRepository.get_by_id(id)
        if not c:
            raise KeyError("Chamado nao encontrado.")
        ChamadoRepository.delete(c)

    @staticmethod
    def iniciar_atendimento(id):
        c = ChamadoRepository.get_by_id(id)
        if not c:
            raise KeyError("Chamado nao encontrado.")

        if c.status != 'Aberto':
            raise ValueError("So pode iniciar chamados com status Aberto.")

        c.status = 'Em atendimento'
        return ChamadoRepository.update(c)

    @staticmethod
    def encerrar_chamado(id):
        c = ChamadoRepository.get_by_id(id)
        if not c:
            raise KeyError("Chamado nao encontrado.")

        if c.status != 'Em atendimento':
            raise ValueError("So pode encerrar chamados que estao Em atendimento.")

        c.status = 'Encerrado'
        return ChamadoRepository.update(c)

    @staticmethod
    def obter_estatisticas():
        return {
            "usuarios": UsuarioRepository.count(),
            "chamados": ChamadoRepository.count(),
            "abertos": ChamadoRepository.count_by_status("Aberto"),
            "em_atendimento": ChamadoRepository.count_by_status("Em atendimento"),
            "encerrados": ChamadoRepository.count_by_status("Encerrado")
        }