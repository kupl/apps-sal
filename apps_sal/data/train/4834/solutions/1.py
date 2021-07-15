def backwardsPrime(start, stop):
    is_prime = lambda n : all(n % a for a in range(3, 1 + int(n ** 0.5), 2)) if n > 2 and n % 2 else n == 2
    
    return [n for n in range(start + ~start % 2, stop + 1, 2) if is_prime(n) and n != int(str(n)[::-1]) and is_prime(int(str(n)[::-1]))]
