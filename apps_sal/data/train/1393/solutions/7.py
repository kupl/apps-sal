for _ in range(int(input())):
 n=int(input())
 c=0
 l=list(map(int,input().split()))
 m=l[0]
 for i in l:
  if m>=i:
   c+=1
   m=i
 print(c)
