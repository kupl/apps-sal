def generateBricks(isCut, y):
    return "{0}|{1}|{0}".format("■" * (1+isCut), '|'.join("■■" for _ in range(y-1-isCut)))

def build_a_wall(*args):
    if len(args) != 2 or any(type(z) != int or z <= 0 for z in args):
        return None
        
    x,y = args
    return ("Naah, too much...here\'s my resignation." if x*y > 10000 
            else '\n'.join( generateBricks((x-nr)%2, y) for nr in range(x) ))
