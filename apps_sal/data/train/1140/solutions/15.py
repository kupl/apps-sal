def ipnl(n): return [int(input()) for _ in range(n)]


def inp(): return int(input())
def ip(): return [int(w) for w in input().split()]


for _ in range(inp()):
    k, ind = ip()
    ans = 0
    while k:
        ans = 2 * ans + ind % 2
        ind //= 2
        k -= 1
    print(ans)
