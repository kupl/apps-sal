from itertools import count
from math import floor
from decimal import Decimal 

#for finding sum upto nth element of arithmetic prograssion starting with a with different d
def find_sum(a, d, n):     
    return int(Decimal(n / 2) * Decimal((2 * a) + ((n - 1) * d)))

#for finding nth term of arithmetic prograssion 
def term(a, d, n):
    return a + (d * (n - 1))

#for solvinng quadratic equation
def solve_quadratic(a, b, c):
    return floor((-b + ((b ** 2) - (4 * a * c)) ** .5) / (2 * a))

#for finding nth value of seq 123456789101112.....
def extract(n):
    passed = 0
    for i in count(1):
        k = 9 * (10 ** (i - 1)) * i
        if passed + k >= n:
            return str(int(10 ** (i - 1) + (n - passed) // i))[int(n - passed) % i]
        passed += k       

def solve(n):     
    n, start, passed = n-1, 1, 0
    for i in count(1):
        k = 9 * 10 ** (i - 1)
        sum_ = find_sum(start, i, k)
    
        if passed + sum_ >= n:
            p = solve_quadratic(i, 2 * start - i, -((n - passed) * 2)) #a, b, c of quad eq
            q = passed + find_sum(start, i, p) 
            return int(extract(n - q))

        start = term(start, i, k) + (i + 1)
        passed += sum_


solve(int(1e100))
