def calculate(*args): 
    try:
        return eval(('').join(map(str, args)))
    except:
        return None
