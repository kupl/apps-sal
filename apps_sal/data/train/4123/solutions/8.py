import math
def lcm(a, b):
    return a * b // math.gcd(a, b)

def divisors(n):
    i, ans = 1, []
    while i**2 <= n:
        if not n % i:
            ans.append(i)
            if i**2 != n: ans.append(n//i)
        i += 1
    return ans

def lcm_cardinality(n):
    ans, divs = 0, divisors(n)
    for i in range(len(divs)):
        for j in range(i, len(divs)):
            if lcm(divs[i], divs[j]) == n:
                ans += 1
    return ans
