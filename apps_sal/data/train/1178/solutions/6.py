# cook your dish here
t=0
try:
 t=int(input())
except:
 pass

for _ in range(t):
 n = int(input())
 a = list(map(int, input().split()))
 
 a = sorted(a)
 
 already_present = 0
 
 for requirement in a:
  
  if already_present>=requirement:
   already_present+=1
 
 print(already_present)
  
  
  

