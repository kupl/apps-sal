(D, X, Y) = map(int, input().split())
T = list(map(int, input().split()))
T.sort()
rokda = D * X
ans = 'YES'
for i in T:
    y = Y
    for j in range(i - 1):
        y = 0.98 * y
    rokda += y
if rokda < 300:
    ans = 'NO'
print(ans)
