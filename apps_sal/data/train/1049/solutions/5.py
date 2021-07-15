# cook your dish here
import sys
t=int(input().strip())
for _ in range(t):
 n, k = map(int, input().strip().split())
 array=list(map(int, input().strip().split()))
 cifre={}
 for el in array:
  cifre[el]=0
 for i in range(k):
  cifre[array[i]]+=1 
 flag=0
 for key in cifre:
  if cifre[key]==0:
   flag=1 
   break
 appo=sum(array[:k])
 somma= appo if flag==0 else 0
 for i in range(0,n-k):
  appo+=array[k+i]-array[i]
  cifre[array[i]]-=1 
  cifre[array[k+i]]+=1 
  flag=0
  for key in cifre:
   if cifre[key]==0:
    flag=1 
    break
  if flag==0:
   somma=max(somma,appo)
 print(somma)
