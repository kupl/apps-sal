from functools import reduce
from math import gcd
def divisor(n):
    i = 3
    while i*i <= n:
        if n%i==0:
            return i
        i+=2
    return n
for _ in range(int(input())):
    n = int(input())
    ls = [int(X)  for X in input().split()]
    gc = reduce(gcd,ls)
    #gcd gives you the greatest common divisor simply printing this is incorrect
    #since gcd divides all the numbers in the array it's divisors will also do the same
    #find the smallest divisor (smallest prime)
    if gc ==1:
        print(-1)
    elif gc %2 ==0:
        print(2)
    else:
        print(divisor(gc))
