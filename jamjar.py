from wsgiref.simple_server import make_server
import cgi
import re

class JamJar(object):
    
    def __init__(self, name):
        self.name = name
        self.routes = {}

    def add_route(self, route, func):
        self.routes[route] = func
        
    def myapp(self, environ, start_response):
        start_response("200 OK", [('Content-Type','text/html')])     
        self.method = environ["REQUEST_METHOD"]
        if self.method == "POST":
            self.data = cgi.FieldStorage(fp=environ["wsgi.input"], environ=environ)            
            return self.routes[environ["PATH_INFO"]](self.data)
        else:
            return self.routes[environ["PATH_INFO"]]()

    def run(self):
        server = make_server('localhost', 8080, self.myapp)
        print "running on http://localhost:8080/..."
        server.serve_forever()
        
    def render_template(self, template, **vars):
        with open(template) as f:
            s = f.read()
            for template_var in vars:
                value = str(vars[template_var])
                s = re.sub(r'{{\s*%s\s*}}' % template_var, value, s)
        return s    
        
 
if __name__ == '__main__':
    jamjar = JamJar(__name__)
    jamjar.run()
