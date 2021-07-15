for _ in range(int(input())):
 n, k = map(int, input().split())
 a = list(map(int, input().split()))
 b = list(map(int, input().split()))

 a = [-1] + a[::-1]
 mx = a.index(max(a))
 dp = [0] * (n + 1)
 for i in range(1, n + 1):
  for x in b:
   if i - x < 0: continue
   if i - x < mx <= i:
    dp[i] = 1
   else:
    dp[i] |= not dp[i - x]

 print('Chef' if dp[-1] else 'Garry')
