def cube_odd(x):
    if len(x)!=len([i for i in x if type(i)==int]):
        return None
    else:
        return sum([i**3 for i in x if i%2!=0])
