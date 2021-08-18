from sys import stdin, setrecursionlimit, stdout
from collections import deque, defaultdict, Counter
from math import log2, log, ceil, sqrt
from operator import *
input = stdin.readline
setrecursionlimit(int(2e5))
def getstr(): return input()[:-1]
def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint1(): return list(map(lambda x: int(x) - 1, input().split()))


def jn(x, l): return x.join(map(str, l))


def swaparr(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def nCr(n, k):
    if(k > n - k):
        k = n - k
    res = 1
    for i in range(k):
        res = res * (n - i)
        res = res / (i + 1)
    return res


def upper_bound(a, x, lo=0):
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def maxSlidingWindow(nums, k):
    windowSum, maxSum = 0, 0
    windowSum = sum(nums[:k])
    for end in range(k, len(nums)):
        windowSum += nums[end] - nums[end - k]
        maxSum = max(maxSum, windowSum)
    return maxSum


def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    return


def prefix(arr):
    a = map(add, arr.insert(0, 0))
    return a


def primefs(n):
    primes = {}
    while(n % 2 == 0):
        primes[2] = primes.get(2, 0) + 1
        n = n // 2
    for i in range(3, int(n**0.5) + 2, 2):
        while(n % i == 0):
            primes[i] = primes.get(i, 0) + 1
            n = n // i
    if n > 2:
        primes[n] = primes.get(n, 0) + 1
    return primes


def power(x, y, p):
    res = 1
    x = x % p
    if (x == 0):
        return 0
    while (y > 0):
        if ((y & 1) == 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


def find(x, link):
    p = x
    while(p != link[p]):
        p = link[p]

    while(x != p):
        nex = link[x]
        link[x] = p
        x = nex
    return p


def union(x, y, link, size):
    x = find(x, link)
    y = find(y, link)
    if size[x] < size[y]:
        x, y = swap(x, y)
    if x != y:
        size[x] += size[y]
        link[y] = x


def sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime


def binsearch(a, l, r, x):
    while l <= r:
        mid = l + (r - 1) // 2
        if a[mid]:
            return mid
        elif a[mid] > x:
            l = mid - 1
        else:
            r = mid + 1
    return -1


graph = defaultdict(list)
visited = [0] * 1000000
col = [-1] * 1000000


def bfs(d, v):
    q = []
    q.append(v)
    visited[v] = 1
    while len(q) != 0:
        x = q[0]
        q.pop(0)
        for i in d[x]:
            if visited[i] != 1:
                visited[i] = 1
                q.append(i)
        print(x)


def make_graph(e):
    d = {}
    for i in range(e):
        x, y = mi()
        if x not in d:
            d[x] = [y]
        else:
            d[x].append(y)
        if y not in d:
            d[y] = [x]
        else:
            d[y].append(x)
    return d


def gr2(n):
    d = defaultdict(list)
    for i in range(n):
        x, y = mi()
        d[x].append(y)
    return d


def connected_components(graph):
    seen = set()

    def dfs(v):
        vs = set([v])
        component = []
        while vs:
            v = vs.pop()
            seen.add(v)
            vs |= set(graph[v]) - seen
            component.append(v)
        return component

    ans = []
    for v in graph:
        if v not in seen:
            d = dfs(v)
            ans.append(d)
    return ans


MAXN = int(1e6 + 5)


def spf_sieve():
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i
    for i in range(4, MAXN, 2):
        spf[i] = 2
    for i in range(3, ceil(MAXN ** 0.5), 2):
        if spf[i] == i:
            for j in range(i * i, MAXN, i):
                if spf[j] == j:
                    spf[j] = i


def factoriazation(x):
    ret = {}
    while x != 1:
        ret[spf[x]] = ret.get(spf[x], 0) + 1
        x = x // spf[x]
    return ret


def lcm(a, b): return abs(a * b) // math.gcd(a, b)


MOD = int(1e9) + 7
CMOD = 998244353
INF = float('inf')
NINF = -float('inf')
y, n = "YES", "NO"
abd = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
       'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
       'z': 25}


def solve():
    n, c, k = map(int, input().split())
    d = {}
    for i in range(n):
        a, b, c = map(int, input().split())
        if c not in d.keys():
            d[c] = 1
        else:
            d[c] += 1
    v = list(map(int, input().split()))
    l_r = k // v[0]
    l = list(d.values())
    i = 0
    while l_r != 0:
        l[l.index(max(l))] -= 1
        l_r -= 1
    count = 0
    for i in l:
        count += ((i) * (i - 1) * (i - 2)) // 6
    print(count)


def __starting_point():
    for _ in range(int(input())):
        solve()


__starting_point()
