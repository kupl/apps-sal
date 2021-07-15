land = lambda a: sum(t == ('X', 'X') for r in a for t in zip(r, r[1:])) * 2

def land_perimeter(a):
    return 'Total land perimeter: ' + str(''.join(a).count('X') * 4 - land(a) - land(zip(*a)))
