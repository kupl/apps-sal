# cook your dish here
t=int(input())

for n in range(t):
 a=str(input())
 b=str(input())
 count = 0
 for i in a:
  for j in b:
   if i==j:
    count+=1
 if count > 0:
  print("Yes")
 else:
  print("No")
