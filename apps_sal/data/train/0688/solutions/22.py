# cook your dish here
t=int(input())

for _ in range(t):
 s=input()
 c=0
 for i in range(len(s)-1):
  
  if s[i]!=s[i+1]:
   c+=1
  
 if c <=2:
  print("uniform")
 else:
  print('non-uniform')
  

