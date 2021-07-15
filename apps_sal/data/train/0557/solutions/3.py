import numpy as py

T=int(input())
for _ in range(T):
 N,M=list(map(int,input().split()))
 l=[10]*N
 for _ in range(M):
  i,j,k=list(map(int,input().split()))
  s1=l[:i-1]
  s2=l[i-1:j]
  s3=l[j:]
  new=list(py.array(s2)*k)
  l=s1+new+s3
  #print(l)
s=sum(l)//N
print(s)

