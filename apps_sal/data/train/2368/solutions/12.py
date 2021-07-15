## necessary imports
import sys
input = sys.stdin.readline
# from math import ceil, floor, factorial;

def ceil(x):
    if x != int(x):
        x = int(x) + 1;
    return x;
    
# swap_array function
def swaparr(arr, a,b):
    temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;

## gcd function
def gcd(a,b):
    if b == 0:
        return a;
    return gcd(b, a % b);

## nCr function efficient using Binomial Cofficient
def nCr(n, k): 
    if(k > n - k): 
        k = n - k; 
    res = 1;
    for i in range(k): 
        res = res * (n - i);
        res = res / (i + 1); 
    return int(res);

## upper bound function code -- such that e in a[:i] e < x;
def upper_bound(a, x, lo=0, hi = None):
    if hi == None:
        hi = len(a);
    while lo < hi:
        mid = (lo+hi)//2;
        if a[mid] < x:
            lo = mid+1;
        else:
            hi = mid;
    return lo;

## prime factorization
def primefs(n):
    ## if n == 1    ## calculating primes
    primes = {}
    while(n%2 == 0 and n > 0):
        primes[2] = primes.get(2, 0) + 1
        n = n//2
    for i in range(3, int(n**0.5)+2, 2):
        while(n%i == 0 and n > 0):
            primes[i] = primes.get(i, 0) + 1
            n = n//i
    if n > 2:
        primes[n] = primes.get(n, 0) + 1
    ## prime factoriazation of n is stored in dictionary
    ## primes and can be accesed. O(sqrt n)
    return primes

## MODULAR EXPONENTIATION FUNCTION
def power(x, y, p): 
    res = 1
    x = x % p  
    if (x == 0) : 
        return 0
    while (y > 0) : 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
        y = y >> 1      
        x = (x * x) % p 
    return res 

## DISJOINT SET UNINON FUNCTIONS
def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b;

# find function with path compression included (recursive)
# def find(x, link):
#     if link[x] == x:
#         return x
#     link[x] = find(link[x], link);
#     return link[x];

# find function with path compression (ITERATIVE)
def find(x, link):
    p = x;
    while( p != link[p]):
        p = link[p];
    
    while( x != p):
        nex = link[x];
        link[x] = p;
        x = nex;
    return p;


# the union function which makes union(x,y)
# of two nodes x and y
def union(x, y, link, size):
    x = find(x, link)
    y = find(y, link)
    if size[x] < size[y]:
        x,y = swap(x,y)
    if x != y:
        size[x] += size[y]
        link[y] = x

## returns an array of boolean if primes or not USING SIEVE OF ERATOSTHANES
def sieve(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return prime

#### PRIME FACTORIZATION IN O(log n) using Sieve ####
MAXN = int(1e5 + 5)
def spf_sieve():
    spf[1] = 1;
    for i in range(2, MAXN):
        spf[i] = i;
    for i in range(4, MAXN, 2):
        spf[i] = 2;
    for i in range(3, ceil(MAXN ** 0.5), 2):
        if spf[i] == i:
            for j in range(i*i, MAXN, i):
                if spf[j] == j:
                    spf[j] = i;
    ## function for storing smallest prime factors (spf) in the array

################## un-comment below 2 lines when using factorization #################
# spf = [0 for i in range(MAXN)]
# spf_sieve();
def factoriazation(x):
    ret = {};
    while x != 1:
        ret[spf[x]] = ret.get(spf[x], 0) + 1;
        x = x//spf[x]
    return ret;
    ## this function is useful for multiple queries only, o/w use
    ## primefs function above. complexity O(log n)

## taking integer array input
def int_array():
    return list(map(int, input().strip().split()));

def float_array():
    return list(map(float, input().strip().split()));

## taking string array input
def str_array():
    return input().strip().split();

#defining a couple constants
MOD = int(1e9)+7;
CMOD = 998244353;
INF = float('inf'); NINF = -float('inf');

################### ---------------- TEMPLATE ENDS HERE ---------------- ###################

for _ in range(int(input())):
    n = int(input());
    a = int_array(); b = int_array();
    ma = min(a); mb = min(b); ans = 0;
    for i in range(n):
        x = a[i] - ma;
        y = b[i] - mb;
        ans += min(x, y);
        ans += abs(x - y);
    print(ans);
