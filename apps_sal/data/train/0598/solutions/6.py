line1 = input().split(' ')
line2 = input().split(' ')
n = int(line1[0])
k = int(line1[1])
moves = k%2

a = [0 for x in range(n)]

for i in range(n):
 a[i] = int(line2[i])

if moves==0:
 moves=2
 
while moves>0:
 m = -20000000000
 for i in range(n):
  if a[i]>m:
   m = a[i]
 
 for i in range(n):
  a[i] = m-a[i]
  
 moves-=1
  
ans = ""

for i in range(n):
 ans+=(str(a[i])+" ")
if k==0:
  ans=""
  for i in range(n):
    ans+=(line2[i]+" ") 
   

print(ans)

