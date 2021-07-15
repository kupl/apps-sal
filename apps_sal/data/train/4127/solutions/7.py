import math
def divisors(n) : 
    ans = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) : 
        if n % i == 0: 
            if n / i == i: 
                ans += 1
            else:
                ans += 2                  
    return ans 

def count_pairs_int(diff, nmax):
    ans = 0
    for val in range(2, nmax-diff):
        if divisors(val) == divisors(val+diff):
            ans += 1
    return ans 
