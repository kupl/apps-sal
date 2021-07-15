# cook your dish here
for _ in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 k=[]
 for i in range(len(l)-1):
  j=l[i]-l[i+1]
  k.append(j)
 print(min(k))
