from itertools import takewhile

squares = {i**2:i for i in range(2, 500)}
cubes = {i**3:i for i in range(2, 500)}
find = lambda n, D: [v for k,v in takewhile(lambda x: x[0] <= n, D.items()) if not n%k]

def factors(n):
    return [find(n, squares), find(n, cubes)]
