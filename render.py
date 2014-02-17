def render_template(template, **var):
    file = open(template)
    s = file.read()
    if var:
        for each in var:
            s = re.sub(r'{{\s*%s\s*}}' %each, str(var[each]), s)
    file.close()    
    return s