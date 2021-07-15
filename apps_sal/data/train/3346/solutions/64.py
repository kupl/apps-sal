import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for x in range(3, int(math.sqrt(n))+1, 2):
        if n % x == 0:
            return False
    return True


def find_first_prime(x1, x2):
    for i in range(x1, x2+1):
        if is_prime(i):
            return i
    return None


def gap(g, m, n):
    try:
        fst = find_first_prime(m, n+1)
        sec = find_first_prime(fst+1, n+1)
        if sec - fst == g:
            return [fst, sec]
        else:
            return gap(g, sec, n)
    except:
        return None

