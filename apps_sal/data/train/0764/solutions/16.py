# cook your dish here
t=int(input())
for i in range(t):
 s1=input().split()
 s2=input().split()
 c=0
 for i in s1:
  for j in s2:
   if i==j:
    c+=1 
 if c>=2:
  print("similar")
 else:
  print("dissimilar")
