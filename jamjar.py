from wsgiref.simple_server import make_server
import cgi
import re

ROUTES = {}

class JamJar(object):
    
    def __init__(self, name):
        self.name = name
        
    def add_route(self, route, func):
        "APPENDS ROUTE TO GLOBAL DICTIONARY"
        self.route = route
        self.func = func
        ROUTES[self.route] = self.func
        
    def myapp(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response
        self.start_response("200 OK", [('Content-Type','text/html')])     
        self.method = self.environ["REQUEST_METHOD"]
        if self.method == "POST":
            self.data = cgi.FieldStorage(fp=environ["wsgi.input"], environ=self.environ)
            return ROUTES[self.environ["PATH_INFO"]](self.data)
        return ROUTES[self.environ["PATH_INFO"]]() 
        
def render_template(template, **var):
    file = open(template)
    s = file.read()
    if var:
        for each in var:
            s = re.sub(r'{{\s*%s\s*}}' %each, str(var[each]), s)
    file.close()    
    return s
        
jamjar = JamJar(__name__)        
        
server = make_server('localhost', 8080, jamjar.myapp)
print "running on http://localhost:8080/..."
 
if __name__ == '__main__':
    server.serve_forever()