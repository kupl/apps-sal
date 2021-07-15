# cook your dish here
t = int(input())
for _ in range(t):
 arr = input().split()
 i1,j1 = 0,0
 for _ in range(int(arr[0])):
  s = str(input())
  if(s[0] == '0'):
   i1+=s.count('0')
  else:
   j1+=s.count('1') 
 if(i1 == j1):
  if(arr[1] == "Dee"):
   print("Dum")
  else:
   print("Dee")
 elif(i1>j1):
  print("Dee")
 else:
  print("Dum")
  
  

