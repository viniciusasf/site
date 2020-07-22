from app import app

@app.route("/index")# personalização de rotas / DECORATOR
@app.route("/")
def index():
    return 'Hello Word' #primeira pagina

@app.route('/test/', defaults={'name': None})
@app.route('/test/<name>')
def test(name): #posso passar o defauts no parâmetro também como None
    if name:
        return f"Olá, {name}!"
    else:
        return 'Olá! Usuário'

