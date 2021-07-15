def factorial(n):
    return n * factorial(n-1) if n > 1 else 1

def strong_num(number):
    return ['Not Strong !!', 'STRONG!!!!'][sum(factorial(int(s)) for s in str(number)) == number]
