# cook your dish here
t=int(input())
while t:
 t=t-1
 n=int(input())
 l=list(map(int,input().split()))
 l.sort(reverse=True)
 c=0
 for i in range(0,n,2):
  c+=l[i]
 print(c)
