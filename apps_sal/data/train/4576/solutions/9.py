def gcd_matrix(a, b):

    def gcd(a2, b2):
        for i in range(min(a2, b2), 0, -1):
            if a2 % i == 0 and b2 % i == 0:
                return i
    output = 0
    for i in a:
        for j in b:
            output += gcd(i, j)
    return round(output / (len(a) * len(b)), 3)
