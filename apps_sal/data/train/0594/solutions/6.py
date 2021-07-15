# cook your dish here
def func1(l):
 if(len(l)==1):
  return 0
 elif(len(l)==2):
  return l[1]-l[0]
 else:
  mid=len(l)//2
  p=l[:mid]
  q=l[mid:]
  return max(func1(p),func1(q),max(q)-min(p))
def func2(l):
 if(len(l)==1):
  return float('inf')
 elif(len(l)==2):
  return l[1]-l[0]
 else:
  mid=len(l)//2
  p=l[:mid]
  q=l[mid:] 
  return min(func2(p),func2(q),min(q)-max(p))
n,x=list(map(int,input().split()))
arr=list(map(int,input().split()))
l=[0]
for i in arr:
 l.append(l[-1]+i)
l.pop(0)
if(x==1):
 print(l[-1])
elif((1/x)-1<0):
 v=func1(l)
else:
 v=func2(l)
print(l[-1]-v+(v/x))




