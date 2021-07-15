from math import sqrt
def sol_equa(n):
    m = [[y, n/y] for y in [x for x in range(1, int(sqrt(n))+1) if n%x == 0]]
    return sorted([[(r[0] +r[1])/2, (r[1] - r[0])/4] for r in [z for z in m if (z[0] +z[1])%2 == 0 and (z[1] - z[0])%4 == 0]], reverse=True)

