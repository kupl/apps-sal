for i in range(int(input())):
 n=int(input())
 m=list(map(int,input().split()))
 if m[0]==1 and m[-1]==1 and n%2!=0 and m[n//2]==max(m):
  for i in range(n//2):
   if abs(m[i+1]-m[i])!=1:
    print("no")
    break
  else:
   print("yes")
 else:
  print("no")
 

