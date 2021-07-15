# cook your dish here
test=int(input())
for _ in range(test):
 n=int(input())
 arr=list(map(int,input().split()))
 pos=0
 num=0
 temp=[]
 for ii in arr:
  if ii>=0:
   pos+=ii
   num+=1
 p=0
 n=0
 for i in range(len(arr)):
  if i<num:
   if arr[i]<0:
    temp.append(i+1)
    n+=1
  else:
   if arr[i]>=0:
    temp.append(i+1)
    p+=1
 print(pos)
 if p==n:
  k=[len(temp)] 
  k.extend(temp)
  print(*k)
 else:
  print(0)
