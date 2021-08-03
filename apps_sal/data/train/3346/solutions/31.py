import math


def isprime(y):
    if all(y % i != 0 for i in range(3, int(math.sqrt(y)) + 1, 2)):
        return True


def gap(g, m, n):
    if m % 2 == 0:
        m = m + 1
    for num in range(m, n, 2):
        if isprime(num) == True:
            for x in range(num + 2, num + g + 1, 2):
                print(x)
                if isprime(x) == True:
                    print((x, num, g))
                    if x - num == g:
                        return [num, x]
                        break
                    else:
                        break
# OH MY GOD IT ACTUALLY WORKED
