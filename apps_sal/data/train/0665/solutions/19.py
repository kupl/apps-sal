def check(month_rat,month_rank,n):
 c=0
 for i in range(1,n+1):
  if(month_rat[i]!=month_rank[i]):
   c+=1
 return c
def ranking(r,m_rank,month_rank,m,n):
 for i in range(m):
  rank=1
  c=0
  for val in r[i]:
   rank+=c
   c=0
   for j in range(n):
    if(val==d[i+1,j+1]):
     if(m_rank[j+1] > rank):
      m_rank[j+1]=rank
      month_rank[j+1]=(i+1)
     c+=1
    
for _ in range(int(input())):
 n,m=list(map(int,input().split()))
 r=list(map(int,input().split()))
 c=[list(map(int,input().split())) for i in range(n)]
 rating=[]
 d={}
 m_rank={}
 m_rat={}
 month_rank={}
 month_rat={}
 f=1
 for i in range(m):
  x=[]
  for j in range(n):
   if(i==0):
    d[(i+1),(j+1)]=r[j]+c[j][i]
    x.append(d[i+1,j+1])
   else:
    d[(i+1),(j+1)]=d[i,(j+1)]+c[j][i]
    x.append(d[i+1,j+1])
   if(f):
    m_rank[j+1]=501
    m_rat[j+1]=d[i+1,j+1]
    month_rat[j+1]=(i+1)
   else:
    if(m_rat[j+1] < d[i+1,j+1]):
     m_rat[j+1]=d[i+1,j+1]
     month_rat[j+1]=(i+1)
  x=list(set(x))
  x.sort()
  rating.append(x[::-1])
  f=0
 ranking(rating,m_rank,month_rank,m,n)
 count=check(month_rat,month_rank,n)
 print(count)
   
   

