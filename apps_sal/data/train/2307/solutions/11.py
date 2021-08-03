def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))


N, A, B = mi()
X = li()
ans = 0
now = X[0]
for x in X[1:]:
    if (x - now) * A > B:
        ans += B
    else:
        ans += (x - now) * A
    now = x
print(ans)
