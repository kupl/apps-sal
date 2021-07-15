for I_I in range(eval(input())):
 n=eval(input())
 count=0
 a=list(map(int,input().split()))
 for ii in range(1,len(a)):
  if a[ii]==a[0]:
   count=count+1
 print(n-count)

