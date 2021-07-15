t = int( input() )

while t > 0:
 n = int( input() )
 s = input()
 c = 0
 z = 1
 
 for i in range( n ):
  if s[i] == '0':
   z += 1
   continue
   
  if z > 2:
   c += z - 2
   
  z = 0
 
 if z > 1:
  c += z - 1

 t -= 1
 print(c) 
