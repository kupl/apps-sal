t = int(input())
for i in range(t):
 n = int(input())
 s = input()
 p = input()
 
 if s == p:
  print("Yes")
 else:
  z1, z2 = s.count("0"), p.count("0")
  
  if z1 != z2:
   print("No")
   continue
  
  counter = 0

  for i in range(n):
   if s[i] != p[i]:
    False
    
    if s[i] == "0":
     if counter > 0:
      counter -= 1
     else:
      counter = 1
      break
    else:
     counter += 1
  
  if counter > 0:
   print("No")
  else:
   print("Yes")
