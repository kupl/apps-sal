# cook your dish here
N,M,K=list(map(int,input().split()))
l1=[]
d={}
for i in range(K):
 l=list(map(int,input().split()))
 l1.append(l)
 if l[1] in d:
  d[l[1]]=d[l[1]]+l.count(l[1])
 elif l[3] in d:
  d[l[3]]=d[l[3]]+l.count(l[1])
 else:
  d[l[1]]=l.count(l[1])
  d[l[3]]=l.count(l[3])
k=max(d, key=d.get)
s=0
for i in range(K):
 s=s+2*(abs(l1[i][1]-k))+2*(abs(l1[i][3]-k))+(abs(l1[i][0]-l1[i][2]))
print(s)
 

