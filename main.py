from bottle import get, run, error
import CodeNameGen

app = bottle.default_app()

@get('/')
def index():
    return "Hello World"

@get('/name')
def random_name():
    return {'name': CodeNameGen.get_code_name()}
    
@error(403)
def error403(code):
    return "Error 403, verboten"
    
@error(404)
def error404(code):
    return "huh?  What are you looking for again?"

if __name__=="__main__":
    run(host='localhost', port=8080)