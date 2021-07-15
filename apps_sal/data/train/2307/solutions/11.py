ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(map(int, input().split()))

N, A, B = mi()
X = li()
ans = 0
now = X[0]
for x in X[1:]:
    if (x-now)*A > B:
        ans += B
    else:
        ans += (x-now)*A
    now = x
print(ans)
