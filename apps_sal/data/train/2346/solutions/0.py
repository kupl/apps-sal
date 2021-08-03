
import sys
# sys.stdin=open("data.txt")
input = sys.stdin.readline
def mii(): return list(map(int, input().split()))


for _ in range(int(input())):
    n, d = mii()
    a = list(mii())
    ans = 0
    for i in range(n):
        while d >= i and a[i]:
            a[i] -= 1
            ans += 1
            d -= i
    print(ans)
