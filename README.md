jamjar
======

JamJar is a a WSGI based web framework that handles get and post requests, and renders variables in HTML. I also created a templating function. App operations as follows:


-- Import  framework and create an instance and run --
```
app = JamJar(__name__)
```


-- Render HTML template --
```
add.route("/url", template_name.html)
```


-- Place variables in HTML templates --
```
add.route("/url", template_name.html, variable1 = variable1, variable2 = variable2)
```


-- Retrieve post request value --
```
variable3 = data.getvalue("variable3")
```

-- Run app as the final command --
```
if __name__ == '__main__':
	app.run()
```



