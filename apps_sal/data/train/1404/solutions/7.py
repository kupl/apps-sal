T = eval(input())

for _ in range(T):
 col = sorted(map(int, input().split()))
 k = eval(input())
 ans = min(col[0], k-1) + min(col[1], k-1) + min(col[2], k-1) + 1
 print(ans)
