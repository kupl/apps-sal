n,m,p=(int(e) for e in input().split())

def add(d,k):
 if k in d:
  d[k]+=1
 else:
  d[k]=1
def get(d,k):
 if k in d:
  return d[k]
 else:
  return 0
dic2={}
dic={}


sumd={}
for i in range(n):
 dic[i]=[]
 sumd[i]=m-1
for i in range(p):
 a,b=(int(e) for e in input().split())
 if b==1:
  sumd[a-1]-=1
 if b==m:
  sumd[a-1]+=1
 add(dic2,(a-1,b-1))
 dic[a-1].append(b-1)


for i in range(n):
 if len(dic[i])<=1:
  print(sumd[i])
 else:
  arr=set(dic[i])
  flag=0
  for e in arr:
   if e==m-1 or get(dic2,(i,e))-1 <= get(dic2,(i,e+1)):
    pass
   else:
    flag=1
    break
  if flag==1:
   print(-1)
  else:
   print(sumd[i])



