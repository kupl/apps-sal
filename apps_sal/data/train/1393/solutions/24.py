for _ in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 count=1
 if len(l)==1:
  print(1)
  continue
 for i in range(1,len(l)):
  if l[i]<l[i-1]:
   count+=1
  elif l[i-1]<l[i]:
   l[i]=l[i-1]
 print(count)
