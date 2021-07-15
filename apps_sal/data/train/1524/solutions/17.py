import sys
t=int(eval(input("")))
while t:
 m,n=list(map(int,sys.stdin.readline().split()))
 prod=n
 prod*=pow((n-1),(m-1),1000000007)
 print(prod%1000000007)
 t-=1

