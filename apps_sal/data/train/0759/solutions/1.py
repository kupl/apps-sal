"""def power(x, y): 
    res = 1
    x=x
    while (y > 0): 
        if ((y & 1) == 1) : 
            res = (res * x) 
        y = y >> 1
        x = (x * x)
    return res"""
"""def fact(n):
    if(n==0):
        return 1
    if(n==1):
        return 1
    return fact(n-1)+fact(n-2)"""




import math
def maxPrimeFactors (n):
    Prime = -1
    while n % 2 == 0:
        Prime = 2
        n >>= 1
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            Prime = i
            n = n / i
    if n > 2:
        Prime = n
    return int(Prime)


array = [0] * 100001
for i in range(1, 100001):
    array[i] = maxPrimeFactors(i)
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    d = {}
    for i in range(n):
        prime_fact = array[arr[i]]
        if prime_fact not in d:
            d[prime_fact] = 1
        else:
            d[prime_fact] += 1
    maxCount = max(d.values())
    ans = -1
    for i in d:
        if(d[i] == maxCount):
            if(i >= ans):
                ans = i
    print(ans)
