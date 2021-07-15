def add_binary(a,b):
    fun = lambda x: fun(x//2) + str(x%2) if x>=1 else ''
    return fun(a+b)
