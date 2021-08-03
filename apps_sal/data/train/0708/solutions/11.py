import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, a = map(int, input().split())
    ans = 0
    prev = a
    fact = 1
    comeon = 1
    for i in range(n):
        comeon = comeon * prev % (10**9 + 7)
        prev = pow(comeon, fact, 10**9 + 7)
        ans = (ans + prev) % (10**9 + 7)
        fact = fact + 2

    print(ans % (10**9 + 7))
