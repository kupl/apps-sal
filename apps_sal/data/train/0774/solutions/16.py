n,k,p=map(int,input().split())
l=list(map(int,input().split()))
t_1=[]
for i in range(n):
 t_1.append([i,l[i]])
t_1=sorted(t_1,key=lambda x:x[1],reverse=True)
dis={}

for i in range(n):
 if i==0:
  dis[i]=t_1[i][1]+k
  continue
 if (t_1[i-1][1]-t_1[i][1])<=k:
  dis[i]=dis[i-1]
 else:
  dis[i]=t_1[i][1]+k
trans={}
for i in range(n):
 trans[t_1[i][0]]=i
for i in range(p):
 a,b=map(int,input().split())
 t_2=a-1
 t_3=b-1
 if dis[trans[t_2]]==dis[trans[t_3]]:
  print('Yes')
 else:
  print('No')
