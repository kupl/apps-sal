try:
 t = int(input())
 for _ in range(t):
  n, k = map(int, input().split())
  qArr = list(map(int, input().split()))
  res = (sum(qArr)//k) + 1
  print(res)
except:
 pass
