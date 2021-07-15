# cook your dish here
t=int(input())
for _ in range(t):
 n,k=list(map(int,input().split()))
 k1=k//n 
 k2=k-(k1*n)
 print(k1)

