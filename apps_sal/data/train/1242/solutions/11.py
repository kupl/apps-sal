# cook your dish here
t=int(input())
for w in range(t):
 n=int(input())
 l=list(map(int,input().split()))
 cost=min(l)
 length=len(l)
 print(cost*(length-1))
