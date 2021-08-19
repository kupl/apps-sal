from fractions import Fraction
import numpy as np
import sys
import bisect
import copyreg
import copy
import statistics
import os
from math import *
from collections import Counter, defaultdict, deque, OrderedDict
from itertools import combinations, permutations, accumulate, groupby
from numpy.linalg import matrix_power as mp
from bisect import bisect_left, bisect_right, bisect, insort, insort_left, insort_right
from statistics import mode
from functools import reduce, cmp_to_key
from io import BytesIO, IOBase
from scipy.spatial import ConvexHull
from heapq import *
from decimal import *
from queue import Queue, PriorityQueue
from re import sub, subn
if sys.version_info[0] < 3:
    from builtins import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip


def bfs(adj, v):
    visited = [False] * (v + 1)
    q = deque()
    while q:
        pass


def graph(vertex):
    return [[] for i in range(vertex + 1)]


def powermodulo(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if y & 1 == 1:
            res = res * x % p
        y = y >> 1
        x = x * x % p
    return res


def lcm(a, b):
    return a * b // gcd(a, b)


def most_frequent(List):
    return Counter(List).most_common(1)[0][0]


def most_common(List):
    return mode(List)


def chinese_remainder(a, p):
    prod = reduce(op.mul, p, 1)
    x = [prod // pi for pi in p]
    return sum((a[i] * powermodulo(x[i], p[i] - 2, p[i]) * x[i] for i in range(len(a)))) % prod


def createMatrix(rowCount, colCount, dataList):
    mat = []
    for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            if dataList[j] not in mat:
                rowList.append(dataList[j])
        mat.append(rowList)
    return mat


def readTree():
    v = int(inp())
    adj = [set() for i in range(v + 1)]
    for i in range(v - 1):
        (u1, u2) = In()
        adj[u1].add(u2)
        adj[u2].add(u1)
    return (adj, v)


def sieve():
    li = [True] * 1000001
    (li[0], li[1]) = (False, False)
    prime = []
    for i in range(2, len(li), 1):
        if li[i] == True:
            for j in range(i * i, len(li), i):
                li[j] = False
    for i in range(1000001):
        if li[i] == True:
            prime.append(i)
    return prime


def setBit(n):
    count = 0
    while n != 0:
        n = n & n - 1
        count += 1
    return count


def digitsSum(n):
    if n == 0:
        return 0
    r = 0
    while n > 0:
        r += n % 10
        n //= 10
    return r


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, list(range(n, n - r, -1)), 1)
    denom = reduce(op.mul, list(range(1, r + 1)), 1)
    return numer // denom


def factors(n):
    return list(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return len(set(factors))


def prefixSum(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i] + arr[i - 1]
    return arr


def binomial_coefficient(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0


def powerOfK(k, max):
    if k == 1:
        return [1]
    if k == -1:
        return [-1, 1]
    result = []
    n = 1
    while n <= max:
        result.append(n)
        n *= k
    return result


def kadane(a, size):
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


def divisors(n):
    result = []
    for i in range(1, ceil(sqrt(n)) + 1):
        if n % i == 0:
            if n / i == i:
                result.append(i)
            else:
                result.append(i)
                result.append(n / i)
    return result


def sumtilln(n):
    return n * (n + 1) // 2


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, ceil(sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def isPowerOf2(n):
    while n % 2 == 0:
        n //= 2
    return True if n == 1 else False


def power2(n):
    k = 0
    while n % 2 == 0:
        k += 1
        n //= 2
    return k


def sqsum(n):
    return n * (n + 1) * (2 * n + 1) // 6


def cusum(n):
    return sumn(n) ** 2


def pa(a):
    for i in range(len(a)):
        print(a[i], end=' ')
    print()


def pm(a, rown, coln):
    for i in range(rown):
        for j in range(coln):
            print(a[i][j], end=' ')
        print()


def pmasstring(a, rown, coln):
    for i in range(rown):
        for j in range(coln):
            print(a[i][j], end='')
        print()


def isPerfectSquare(n):
    return pow(floor(sqrt(n)), 2) == n


def nC2(n, m):
    return n * (n - 1) // 2 % m


def modInverse(n, p):
    return powermodulo(n, p - 2, p)


def ncrmodp(n, r, p):
    num = den = 1
    for i in range(r):
        num = num * (n - i) % p
        den = den * (i + 1) % p
    return num * powermodulo(den, p - 2, p) % p


def reverse(string):
    return ''.join(reversed(string))


def listtostr(s):
    return ' '.join([str(elem) for elem in s])


def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def isarrayodd(a):
    r = True
    for i in range(len(a)):
        if a[i] % 2 == 0:
            r = False
            break
    return r


def isPalindrome(s):
    return s == s[::-1]


def gt(x, h, c, t):
    return (x * h + (x - 1) * c) / (2 * x - 1)


def CountFrequency(my_list):
    freq = {}
    for item in my_list:
        freq[item] = freq[item] + 1 if item in freq else 1
    return freq


def CountFrequencyasPair(my_list1, my_list2, freq):
    for item in my_list1:
        freq[item][0] = freq[item][0] + 1 if item in freq else 1
    for item in my_list2:
        freq[item][1] = freq[item][1] + 1 if item in freq else 1
    return freq


def binarySearchCount(arr, n, key):
    left = 0
    right = n - 1
    count = 0
    while left <= right:
        mid = int((right + left) / 2)
        if arr[mid] <= key:
            (count, left) = (mid + 1, mid + 1)
        else:
            right = mid - 1
    return count


def primes(n):
    (sieve, l) = ([True] * (n + 1), [])
    for p in range(2, n + 1):
        if sieve[p]:
            l.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return l


def Next_Greater_Element_for_all_in_array(arr):
    (s, n, reta, retb) = (list(), len(arr), [], [])
    arr1 = [list([0, i]) for i in range(n)]
    for i in range(n - 1, -1, -1):
        while len(s) > 0 and s[-1][0] <= arr[i]:
            s.pop()
        if len(s) == 0:
            arr1[i][0] = -1
        else:
            arr1[i][0] = s[-1]
        s.append(list([arr[i], i]))
    for i in range(n):
        reta.append(list([arr[i], i]))
        retb.append(arr1[i][0])
    return (reta, retb)


def polygonArea(X, Y, n):
    area = 0.0
    j = n - 1
    for i in range(n):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i
    return abs(area / 2.0)


def merge(a, b):
    ans = defaultdict(int)
    for i in a:
        ans[i] += a[i]
    for i in b:
        ans[i] += b[i]
    return ans


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


class segtree:

    def __init__(self, n):
        self.m = 1
        while self.m < n:
            self.m *= 2
        self.data = [0] * (2 * self.m)

    def __setitem__(self, i, x):
        x = +(x != 1)
        i += self.m
        self.data[i] = x
        i >>= 1
        while i:
            self.data[i] = self.data[2 * i] + self.data[2 * i + 1]
            i >>= 1

    def __call__(self, l, r):
        l += self.m
        r += self.m
        s = 0
        while l < r:
            if l & 1:
                s += self.data[l]
                l += 1
            if r & 1:
                r -= 1
                s += self.data[r]
            l >>= 1
            r >>= 1
        return s


class FenwickTree:

    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, x, d):
        while x <= self.n:
            self.bit[x] += d
            x += x & -x

    def query(self, x):
        res = 0
        while x > 0:
            res += self.bit[x]
            x -= x & -x
        return res

    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)


if os.path.exists('in.txt'):
    sys.stdin = open('in.txt', 'r')


def inp():
    return sys.stdin.readline().strip()


def out(var):
    sys.stdout.write(str(var))


def I():
    return inp()


def II():
    return int(inp())


def FI():
    return float(inp())


def SI():
    return list(str(inp()))


def MI():
    return map(int, inp().split())


def LI():
    return list(MI())


def SLI():
    return sorted(LI())


def MF():
    return map(float, inp().split())


def LF():
    return list(MF())


def SLF():
    return sorted(LF())


MOD = 998244353
mod = 10 ** 9 + 7


def __starting_point():
    (n, k) = MI()
    x = []
    for ii in range(n):
        x.append(set(LI()[1:]))
    v = {}
    v[0] = True
    q = [x[0]]
    for ele in q:
        for j in range(n):
            if not v.get(j, False):
                if len(ele.intersection(x[j])) >= k:
                    q.append(x[j])
                    v[j] = True
    print(len(q))


__starting_point()
