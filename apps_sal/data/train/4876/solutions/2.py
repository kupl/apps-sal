def hello(name=None):    
    if not name:
        return "Hello, World!"
    return "Hello, %s!"%(name.capitalize())
