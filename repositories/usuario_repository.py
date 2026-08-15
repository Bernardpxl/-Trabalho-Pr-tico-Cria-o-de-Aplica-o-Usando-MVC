from database import db
from models.usuario import Usuario

class UsuarioRepository:
    @staticmethod
    def get_all():
        return Usuario.query.all()

    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)

    @staticmethod
    def get_by_email(email):
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def create(usuario):
        db.session.add(usuario)
        db.session.commit()
        return usuario

    @staticmethod
    def update(usuario):
        db.session.commit()
        return usuario

    @staticmethod
    def delete(usuario):
        db.session.delete(usuario)
        db.session.commit()

    @staticmethod
    def count():
        return Usuario.query.count()