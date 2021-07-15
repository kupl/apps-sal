def compute_hcf(x,y):
 if x > y:
  smaller = y
 else:
  smaller = x
 lst=[]
 for i in range(1, smaller+1):
  if((x % i == 0) and (y % i == 0)):
   lst.append(i)
 return (max(lst))
t=int(input())
for i in range(t):
 a,b=map(int,input().split())
 print(compute_hcf(a,b))
