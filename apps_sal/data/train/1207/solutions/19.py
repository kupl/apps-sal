# cook your dish here
for t in range(int(input())):
 n = int(input())
 p = list(map(int, input().split()))
 m = min(p)
 s = 0
 for i in p:
  if i != m:
   s += i*m
 print(s)
