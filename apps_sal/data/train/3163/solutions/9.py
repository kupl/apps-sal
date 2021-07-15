def triangular_sum(t):
    triangles = [1]
    n = 2
    while triangles[-1] < t**0.5:
        triangles.append(triangles[-1] + n)
        n += 1
    for n1 in triangles:
        for n2 in triangles:
            if n1 != n2 and n1*n1 + n2*n2 == t:
                return True
    return False

