Trabalho Pr�tico - API Helpdesk
Aluno: [Bernardo Garajau Silva]

Como rodar a aplica��o:

1. Instalar o Flask e o SQLAlchemy:
pip install flask flask_sqlalchemy

2. Executar o projeto:
python app.py

A API vai rodar em http://127.0.0.1:5000/ e o banco de dados (helpdesk.db) � criado sozinho na raiz.

Rotas do sistema:

- GET /usuarios
- POST /usuarios
- PUT /usuarios/<id>
- DELETE /usuarios/<id>
- GET /usuarios/<id>/chamados

- GET /chamados
- POST /chamados
- PUT /chamados/<id>
- DELETE /chamados/<id>
- PATCH /chamados/<id>/iniciar
- PATCH /chamados/<id>/encerrar
- GET /chamados/abertos
- GET /chamados/prioridade/alta

- GET /estatisticas
