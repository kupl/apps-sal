# cook your dish here
t,x=map(int,input().split())
for _ in range(t):
 n=int(input())
 if n<0:
  temp=n+((int(abs(n)**.5))**2)
 else:
  temp=n-((int(n**.5))**2)
 n=(float(n)*float(x))/100.0
 #n*x/100.0
 if temp<=n:
  print("yes")
 else:
  print("no")
