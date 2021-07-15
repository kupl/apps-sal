# cook your dish here
a = int(input())
for i in range(a):
 b = int(input())
 c = list(map(int,str(input()).split(' ')))
 c.sort()
 n = 0
 for j in range(b):
  if int(c[j])<=j:
   n+=1
  else:
   break
 print(n)
