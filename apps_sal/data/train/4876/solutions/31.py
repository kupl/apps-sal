def hello(*args):
    try:
        name = str(args[0])
        return "Hello, " + name[0].upper() + name[1:].lower() + "!"
    except: 
        return "Hello, World!"
    

