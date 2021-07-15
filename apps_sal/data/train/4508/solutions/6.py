from itertools import combinations

vampires = set()
for i in [1, 2]:
    for x, y in combinations(range(10**i, 10**(i+1)), 2):
        if x % 10 == 0 == y % 10:
            continue
        z = x * y
        if sorted(str(z)) == sorted(f'{x}{y}'):
            vampires.add(z)
xs = sorted(vampires)

def VampireNumber(i):
    return xs[i-1]
