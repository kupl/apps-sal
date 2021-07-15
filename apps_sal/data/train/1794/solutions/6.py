def isPrime(n):
    return n is 2 or n % 2 is not 0 and all(n % i != 0 for i in range(3, int(n ** 0.5) + 1, 2))

def statement1(s):
    return not (s % 2 is 0 or isPrime(s - 2))

def statement2(p):
    return sum(statement1(i + int(p / i)) for i in range(2, int(p ** 0.5) + 1) if p % i == 0) is 1

def statement3(s):
    return sum(statement2(i * (s - i)) for i in range(2, int(s / 2) + 1)) is 1

def is_solution(a, b):
    return statement3(a + b)
