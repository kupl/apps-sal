for _ in range(int(input())):
 n = int(input())
 k = int(input())
 if k % n == 0:
  print(0)
 else:
  low = min(k % n, n-k % n)
  print(min(n-1, low*2))
