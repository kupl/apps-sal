from math import factorial

def sum_arrangements(n):
    s = str(n)
    return (10**len(s)-1)//9*sum(map(int,s))*factorial(len(s)-1)
