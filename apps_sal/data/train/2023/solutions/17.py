from math import sqrt
n=int(input())
k=int(sqrt(n))
while(n):
    if n>k-1:
        for i in range(n-k+1,n+1):
            print(i,end=' ')
        n-=k
    if n!=0 and n<k:
        for i in range(1,n+1):
            print(i,end=' ')
        n=0
  

