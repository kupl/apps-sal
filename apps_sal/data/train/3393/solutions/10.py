def divi(n):
    fac = set()
    for i in range(1, int(n**.5) + 1):
        if n % i == 0:
            fac.add(i**2)
            fac.add(int(n / i)**2)
    return fac


def list_squared(m, n):
    return [[i, sum(divi(i))] for i in range(m, n) if str(sum(divi(i))**.5)[-1] == '0']
