for i in range(eval(input())):
 n=eval(input())
 c=0
 l=list(map(int, input().split()))
 for j in range(1,n+1):
  if l[0]<l[j]:c+=1
 print(c)
