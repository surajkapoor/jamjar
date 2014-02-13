from wsgiref.simple_server import make_server
import cgi
import re
 
ROUTES = {}

def render_template(template, **var):
    file = open(template)
    s = file.read()
    if var:
        for each in var:
            s = re.sub(r'{{\s*%s\s*}}' %each, str(var[each]), s)
    file.close()    
    return s
    
def add_route(route, func):
    ROUTES[route] = func  
     
def myapp(environ, start_response):
    start_response("200 OK", [('Content-Type','text/html')])
    method = environ["REQUEST_METHOD"]
    if method == "POST":
        data = cgi.FieldStorage(fp=environ["wsgi.input"], environ=environ) 
        value = data.getvalue("fullname")
        return ROUTES[environ["PATH_INFO"]](), value
    return ROUTES[environ["PATH_INFO"]]()
        
server = make_server('localhost', 8080, myapp)
print "running on http://localhost:8080/..."
 
if __name__ == '__main__':
    server.serve_forever()