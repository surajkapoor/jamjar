from jamjar import server, add_route, render_template

def home():
    age = 18
    name = "SURAJ"
    return render_template("hello.html", name = name, age = age, school = "HACKER SCHOOL")
    
add_route('/', home)    
    
def postpage():
    return render_template("post.html")
    
def            
                 
add_route('/postpage', postpage)



server.serve_forever()        

#{func: posturl, value} 