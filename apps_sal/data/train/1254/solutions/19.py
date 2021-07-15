# cook your dish here
for _ in range(int(input())):
 n,p = list(map(int,input().split()))
 l = list(map(int,input().split()))
 e,h = 0,0 
 for i in l:
  if i<=p//10:
   h+=1 
  elif i>=p//2:
   e+=1 
 if e==1 and h==2:
  print("yes")
 else:
  print("no")

