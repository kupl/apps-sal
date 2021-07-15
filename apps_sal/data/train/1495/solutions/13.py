def check1(array):
 last=[0 for i in range(10)]
 for i in range(10):
  last[i]=array[i]-array[i]%3
  array[i]=array[i]%3
 j=9
 while j>=0:
  if j%3==0:
   last[j]+=array[j]
  else:
   for i in range(j-1,0,-1):
    if (j+i)%3==0:
     while array[j]!=0 and array[i]!=0:
      last[j]+=1
      last[i]+=1
      array[j]-=1
      array[i]-=1
  j-=1
 ans=[str(i)*last[i] for i in range(10)]
 return int(''.join(ans[::-1]))

def check2(array):
 last=[0 for i in range(10)]
 j=9
 while j>=0:
  if j%3==0:
   last[j]=array[j]
   array[j]=0
  else:
   for i in range(j-1,0,-1):
    if (j+i)%3==0:
     while array[j]!=0 and array[i]!=0:
      last[j]+=1
      last[i]+=1
      array[j]-=1
      array[i]-=1
  j-=1
 for i in range(10):
  last[i]+=array[i]-array[i]%3
 ans=[str(i)*last[i] for i in range(10)]
 return int(''.join(ans[::-1]))
 



T=int(input().strip())
for i in range(T):
 N=int(input().strip())
 array=[0 for i in range(10)]
 arr=list(map(int,input().strip().split()))
 for j in arr:
  array[j]+=1
 if array[0]==0:
  print(-1)
 else:
  array1=array[:]
  a=check1(array)
  b=check2(array1)
  print(max(a,b))
  

