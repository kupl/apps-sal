def factorTwos(n):
    twos = 0
    while not n % 2:
        n //= 2
        twos += 1
    
    return (twos, n)
    
#not the prettiest, but it works
def sharkovsky(a, b):
    twosA, remA = factorTwos(a)
    twosB, remB = factorTwos(b)
    
    if remA == 1:
        return remB == 1 and twosA > twosB
    elif remB == 1:
        return remA != 1 or twosA > twosB
    elif twosA == twosB:
        return remA < remB
    else:
        return twosA < twosB
