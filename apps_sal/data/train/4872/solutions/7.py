class F:
 def __init__(S,*a):S.a=a
 compute=lambda S:__import__("operator").__dict__[type(S).__name__](*(x.compute()for x in S.a))
class value(F):compute=lambda S:S.a[0]
class add(F):pass
class sub(F):pass
class mul(F):pass
class truediv(F):pass
class mod(F):pass
class pow(F):pass
