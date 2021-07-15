t = int(input())
while t > 0:
 n = int(input())
 k = int(input())
 high = k % n
 low = n - high
 if high == low:
  ans = 2 * high - 1
  print(ans)
 else: 
  mn = min(high, low)
  ans = 2 * mn
  print(ans)
 t = t - 1



