# cook your dish here
t = int(input())
for i in range(t):
 a,b,c=[int(x) for x in input().split()]
 y= min(a,b)
 z=max(a,b)
 if y+c >= z :
  print(0)
 else:
  print(z-(y+c))
