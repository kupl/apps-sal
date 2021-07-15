basic_op = lambda o, v1, v2: __import__("operator").__dict__[{"+":"add","-":"sub", "*":"mul", "/":"truediv"}[o]](v1,v2)
