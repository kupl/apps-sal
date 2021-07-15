for _ in range(int(input())):
 
 n,k = map(int, input().split())
 
 s = input()
 
 uppercase,lowercase = 0,0
 
 for i in s:
  
  if i >= 'a' and i <= 'z':
   
   lowercase += 1
   
  elif i >= 'A' and i <= 'Z':
   
   uppercase += 1
   
 if uppercase <= k and lowercase <= k:
  
  print("both")
  
 elif uppercase <= k and lowercase > k:
  
  print("chef")
  
 elif uppercase > k and lowercase <= k:
  
  print("brother")
  
 else:
  
  print("none")
