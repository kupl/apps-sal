from itertools import permutations as perms
def prime_seive(n):
    nums = range(n)
    for i1 in nums:
        if i1 > 1:
            for i2 in range(i1*2,n,i1):
                nums[i2] = 0
    return [i for i in nums if i > 1]

def prime(n):
    if n % 2 == 0 or n < 3:return n == 2
    for i in range(3,int(n ** 0.5)+1,2):
        if n % i == 0:return False
    return True

def prime_perms(p,m):
    ans = []
    for i in perms(str(p)):
        s = ''.join(i)
        num = int(s)
        if num == p:continue
        if num < m and prime(num):
            if len(str(num)) != len(s):continue
            if num < p:
                ans = []
                break
            if not num in ans:ans += [num]
    return ans


def find_prime_kPerm(n,k):
    primes = prime_seive(n)
    ans = []
    for p in primes:
        perm = prime_perms(p,n)
        l = len(perm)
        if l == k:
            ans += [p]
    return [len(ans),ans[0],ans[-1]] if len(ans) > 0 else [0,0,0]
