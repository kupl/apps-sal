def array_madness(a,b):
    return sum(n * n for n in a) > sum(n * n * n for n in b) 
