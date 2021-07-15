def sito(m, n):
    """Sito Erastotenesa"""
    numbers = [x for x in range(0, n+1)]
    numbers[0], numbers[1] = False, False
    primes = {}
    for i,x in enumerate(numbers):
        if x:
            if x >= m:
                primes[x] = x
            index = i**2
            while index < len(numbers):
                numbers[index] = False
                index += x
    return primes
                

def primes_a_p(lower_limit, upper_limit):
    primes = sito(lower_limit, upper_limit)
    longest_gap = (upper_limit-lower_limit) // 5
    ap_primes = []
    for i in list(primes.keys()):
        for gap in range(2,longest_gap, 2):
        
            if primes[i]+5*gap <= upper_limit:
                check = [primes[i]+n*gap for n in range(0,6)]
                if any(num not in primes for num in check):
                    pass
                else:
                    ap_primes.append(check)
    return ap_primes

