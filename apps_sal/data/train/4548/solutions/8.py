from functools import reduce
def fib(n):    
    array = []
    a, b = 0, 1
    while a < n + 1:
        array.append(a)
        a, b = b, a+b
    return array

def SumEvenFibonacci(limit): 
    array = fib(limit)
    resultado = list(filter(lambda x: x % 2 == 0, array))
    return reduce((lambda x, y: x + y), resultado ) 
