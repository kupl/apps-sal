for _ in range(int(input())):
 name = str(input())
 c = 0
 for a in name:
  if a.isalpha():
   if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':   
    c = c*10 + 0
   else:
    c = c*10 + 1 
  
 s = str(c)
 a = int(s,2)
 print(a % (10**9 + 7) )

