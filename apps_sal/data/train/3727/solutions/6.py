def pythagorean_triplet(n):
    for z in range(1, int(n**0.5) + 1): # z is hypotenuse
        y = n / z # y is a * b
        if y.is_integer():
            x = (z**2 + 2*y) ** 0.5 # (a + b)
            if x.is_integer():
                for a in range(1, int(x)):
                    b = x - a
                    if a*b == y:
                        return sorted([a,b,z])
