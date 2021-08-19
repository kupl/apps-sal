# standard prime checker algo
def isPrime(n):
    # corner points
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if(n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True


def gap(gap_size, start_srch, end_srch):
    while start_srch <= end_srch:
        if isPrime(start_srch) and isPrime(start_srch + gap_size) and not any(map(isPrime, range(start_srch + 1, start_srch + gap_size))):
            return [start_srch, start_srch + gap_size]
        else:
            start_srch += 1
    return None
