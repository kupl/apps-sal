def backwardsPrime(start, stop):
    return [x for x in range(start, stop+1) if is_prime(x) and is_prime(int(str(x)[::-1])) and str(x) != str(x)[::-1]]

def is_prime(n):
    return all(n%x for x in range(2, int(n**.5+1)))
