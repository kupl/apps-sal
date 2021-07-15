def array_madness(a,b):
    return sum(map(square, a)) > sum(map(cube, b))

def square(x):
    return x*x

def cube(x):
    return x*x*x
