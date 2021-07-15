# cook your dish here
t=int(input())
for i in range(t):
 s=input()
 ans=1
 for j in s:
  if(s.count(j)>1):
   ans=0
   break
 if(ans==0):
  print("yes")
 else:
  print("no")

