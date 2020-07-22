from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager



app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)# Instanciando para cuidar das migrações para isso recebe a aplicação e o banco de dados
#vai trabalhar com as migrações.


mananger = Manager(app)# vai cuidar dos comandos, o primeiro é o (runserver, comando de execução)
mananger.add_command('db', MigrateCommand)# aqui adiciona comandos não precisamos passar o que o db faz, isso já vem
# pronto no formato do MigrateCommand já faz tudo automaticamente já vem pronto e preparado os comandos.

#commandos
#python run.py db migrate
#python run.py db update
#executar esses 2 comandos para qualquer alteração na estrutura do db
from app.controllers import defaut


