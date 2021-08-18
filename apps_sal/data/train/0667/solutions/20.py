import sys
input = sys.stdin.readline
inp, ip = lambda: int(input()), lambda: [int(w) for w in input().split()]

for _ in range(1, int(input()) + 1):
    n, d = map(int, input().split())
    x = [int(w) for w in input().split()]
    ans = []
    ans.append(x[-1] * (d // x[-1]))
    prev = ans[0]
    for i in reversed(range(n - 1)):
        ans.append(x[i] * (prev // x[i]))
        prev = ans[-1]
    print(min(ans))
