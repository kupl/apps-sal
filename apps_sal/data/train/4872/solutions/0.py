import operator as o
class v:
    def __init__(s,a,b): s.a,s.b=a,b
    def compute(s): return getattr(o,type(s).__name__)(s.a,s.b)
class value(int): pass
class add(v): pass
class sub(v): pass
class mul(v): pass
class truediv(v): pass
class mod(v): pass
class pow(v): pass
