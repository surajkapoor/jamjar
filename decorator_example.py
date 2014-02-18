ROUTES = {}

def route(url):
    def func(func):
        def func2(*args, **kwargs):
            print args
            print kwargs
            ROUTES[url] = func, args
            return
        return func2         
    return func    

@route('/url')
def url(n):
    return n
    
print url(5)
print ROUTES