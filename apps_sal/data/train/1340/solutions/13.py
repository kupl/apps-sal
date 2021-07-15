def solve():
 n = int(input())
 l = list(map(int, input().split()))

 s = 0
 p = 0

 for i in l:
  if(i>=0):
   p+=1
   s+=i

 if(p == 0):
  return [0,[]]

 ans = []
 for i in range(0,p):
  if(l[i] <0):
   ans.append(i+1)

 for i in range(p, n):
  if(l[i]>=0):
   ans.append(i+1)


 return [s, ans]

for _ in range(int(input())):
 p = solve()
 print(p[0])
 p1 = [len(p[1])] + p[1]
 print(*p1)
  

 
 


 
   

 

 

 

