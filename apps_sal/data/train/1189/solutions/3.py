from collections import defaultdict
t = int(input())
queries = []
while t:
    t -= 1
    n = int(input())
    queries.append(list(map(int, input().split())))


def solve(a, n):
    su = sum(a)
    mp = defaultdict(int)
    s = 0
    ans = 0
    for i in range(n):
        if((su - a[i]) % 2 == 0):
            ans += mp[(su - a[i]) // 2]
        s += a[i]
        mp[s] += 1
    mp.clear()
    s = 0
    for i in range(n - 1, -1, -1):
        if((su - a[i]) % 2 == 0):
            ans += mp[(su - a[i]) // 2]
        s += a[i]
        mp[s] += 1
    return ans


for i in queries:
    print(solve(i, len(i)))
