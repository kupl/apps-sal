# cook your dish here
t = int (input())
while t > 0:
 n = int(input())
 l = list(map(int,input().strip().split()))[:n]
 s = sum(l)
 if s >= 0:
  print("YES")
 else :
  print("NO")
 t = t - 1

