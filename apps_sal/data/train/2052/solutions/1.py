import sys
(n, m) = list(map(int, input().split()))
Rowsr = [True] * n
Rowsr[0] = False
Rowsr[-1] = False
Rowsl = [True] * n
Rowsl[0] = False
Rowsl[-1] = False
Colu = [True] * n
Colu[0] = False
Colu[-1] = False
Cold = [True] * n
Cold[0] = False
Cold[-1] = False
for i in range(m):
    (a, b) = list(map(int, sys.stdin.readline().split()))
    Rowsr[a - 1] = False
    Colu[b - 1] = False
    Rowsl[a - 1] = False
    Cold[b - 1] = False
ans = 0
for i in range(n // 2):
    x = [Rowsr[i], Rowsr[n - 1 - i], Colu[i], Colu[n - 1 - i]]
    ans += x.count(True)
if n % 2 == 1:
    if Rowsr[n // 2] or Colu[n // 2]:
        ans += 1
print(ans)
