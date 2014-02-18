from jamjar import JamJar, render_template

app = JamJar(__name__)

def home():
    age = 18
    name = "SURAJ"
    return render_template("hello.html", name = name, age = age, school = "HACKER SCHOOL")
   
app.add_route('/', home)    

def get_namepage():
    return render_template("namepage.html")                  
                 
app.add_route('/namepage', get_namepage)

def data(data):
    radio = data.getvalue("radio")
    return render_template('data.html', radio = radio)
    
app.add_route('/data', data)

if __name__ == '__main__':
	app.run()

