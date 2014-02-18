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
        self.environ = environ
        self.start_response = start_response
        self.start_response("200 OK", [('Content-Type','text/html')])     
        self.method = self.environ["REQUEST_METHOD"]
        if self.method == "POST":
            self.data = cgi.FieldStorage(fp=environ["wsgi.input"], environ=self.environ)            
            try:
                self.data.getvalue(self.data.keys()[0])
            except IndexError:
                return "You didn't select an option"    
            return self.routes[self.environ["PATH_INFO"]](self.data)
        return self.routes[self.environ["PATH_INFO"]]()

    def run(self):
        server = make_server('localhost', 8080, self.myapp)
        print "running on http://localhost:8080/..."
        server.serve_forever()
        
def render_template(template, **var):
    file = open(template)
    s = file.read()
    if var:
        for each in var:
            s = re.sub(r'{{\s*%s\s*}}' %each, str(var[each]), s)
    file.close()    
    return s    
        
 
if __name__ == '__main__':
    jamjar = JamJar(__name__)
    jamjar.run()
