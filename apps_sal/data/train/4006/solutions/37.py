basic_op = lambda o,v1,v2: int.__dict__[{"+":"__add__","-":"__sub__","*":"__mul__","/":"__truediv__"}[o]](v1,v2)
