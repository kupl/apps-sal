
def ns(): return input()
def ni(): return int(input())
def nm(): return map(int, input().split())
def nl(): return list(map(int, input().split()))


for _ in range(ni()):
    n = ni()
    a = nl()
    a.sort()
    ans = a[-1]
    for i in range(1, n):
        ans = (ans + a[n - 1 - i]) / 2
    print(ans)
