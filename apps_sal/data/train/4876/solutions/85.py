def hello(name=""):
    return "Hello, {}".format(name[0].upper()+name[1:].lower()+"!") if len(name) > 0 else "Hello, World!"
