def eo(n):
 cnt=0
 while(n):
  n&=n-1
  cnt+=1
 return cnt

def xor(a, b):
 ans = a^b
 return ans

for _ in range(int(input())):
 arr=[]
 even=0
 odd=0
 check={}
 for _ in range(int(input())):
  x=int(input())
  if check.get(x)==None:
   for i in range(len(arr)):
    y=xor(x, arr[i])
    if check.get(y)==None:
     check[y]=0
     arr.append(y)
     j=eo(y)
     if j%2==0:
      even+=1
     else:
      odd+=1
  if check.get(x)==None:
   check[x]=0
   arr.append(x)
   j=eo(x)
   if j%2==0:
    even+=1
   else:
    odd+=1
  print(even,odd)
