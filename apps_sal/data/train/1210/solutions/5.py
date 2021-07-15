# cook your dish here
for _ in range(int(input())):
 n, x=map(int,input().strip().split())
 lr, he=input().strip().split()
 if lr == "R":
  x=n-x+1
 if he == "H":
  if x%2==0:
   ans="E"
  else:
   ans="H"
 elif he == "E":
  if x%2==0:
   ans="H"
  else:
   ans="E"
 print(x,ans)
