def hello(name = ''):
    if(name != ''):
        return "Hello, " + name.lower().title() + "!"
    return "Hello, World!"
