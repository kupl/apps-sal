for _ in range(eval(input())):
 n=eval(input())
 a=list(map(int,input().split()))
 c=0
 for i in range(1,n+1):
  if a[0]<a[i]:
   c+=1
 print(c) 
