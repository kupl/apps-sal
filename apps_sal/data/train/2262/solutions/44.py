r,c,n=map(int,input().split())
def po(x,y):
  if y==0:return x
  if x==r:return r+y
  if y==c:return r+c+(r-x)
  if x==0:return r+c+r+(c-y)
q=[]
for i in range(n):
  x1,y1,x2,y2=map(int,input().split())
  if (x1 in [0,r] or y1 in [0,c])and(x2 in [0,r] or y2 in [0,c]):
    q.append((po(x1,y1),i))
    q.append((po(x2,y2),i))
if len(q)==0:print("YES");return
q.sort()
d=[]
for _,i in q:
  if len(d)==0:d.append(i)
  elif d[-1]==i:del d[-1]
  else:d.append(i)
if len(d)==0:print('YES')
else:print('NO')
