# cook your dish here
for i in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 k=[]
 for i in range(len(l)):
  r=l.count(l[i])
  k.append(r)
 s=max(k)
 print(len(l)-s)
