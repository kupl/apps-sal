N = int(input())
m = 10 ** 9
ans = 0
for i in range(N):
    (A, B) = map(int, input().split())
    ans += B
    if A > B:
        m = min(m, B)
if m == 10 ** 9:
    print(0)
else:
    print(ans - m)
