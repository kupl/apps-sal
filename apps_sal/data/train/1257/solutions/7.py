t=eval(input())
t=int(t)
for i in range(0,t):
 n=eval(input())
 n=int(n)
 if n==0:
  n=1
 for j in range(2,n):
  n*=j
 print(n) 

