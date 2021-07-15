import math

def gap(g, m, n):
    def isPrime(num):
        for i in range(2, math.floor(num**0.5) + 1):
            if num % i == 0: return False
        return True
    last = None
    for num in range(m, n+1):
        if isPrime(num): 
            if last and (num - last == g):
                return [last, num]
            last = num

