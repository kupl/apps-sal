t = int(input())
for _ in range(t):
 n, m, x, y = (int(x) for x in input().split())
 a = (n-1)%x == 0 and (m-1)%y == 0
 b = (n-2)%x == 0 and (m-2)%y == 0 and min(n,m)>1
 if a or b :
  print("Chefirnemo")
 else:
  print("Pofik")
