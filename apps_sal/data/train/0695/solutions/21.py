# cook your dish here
 

for _ in range(int(input())) :
 x, y, n = map(int,input().split())
 counter = 0
 
 for i in range(n+1) :
  if x^i < y^i :
   counter += 1
   
 print(counter)
