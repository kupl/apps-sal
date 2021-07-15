from math import pow
t=input()
t=int(t)
while t>0:
 n,k=input().split()
 n=int(n)
 k=int(k)
 p=pow(k-1,n-1)
 tot=(k*p)%(pow(10,9)+7)
 print(int(tot))
 t=t-1
