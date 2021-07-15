import sys

k=1
l=[]
n=1
while n<=1000:
 l.append(k)
 k=k*(2*n+1)
 n+=1

t = int(input())

for i in range(t):
 n=int(input())
 print(l[n-1])



return

