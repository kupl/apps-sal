import math
def summationOfPrimes(primes):
    ans = 0
    for num in range(2,primes + 1):
        if all(num%i!=0 for i in range(2, int(math.sqrt(num))+1)):
            ans += num
    return ans

