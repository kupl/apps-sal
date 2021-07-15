for _ in range(int(input())):
 t = int(input())
 s = input()
 b = 0
 g = 0
 for i in s:
  if i=='B':
   b+=1
  else:
   g+=1
 if abs(g-b)>1:
  print("-1")
 elif (g-b)>0:
  gl = []
  bl = []
  for i in range(len(s)):
   if s[i]=='B' and i%2==0:
    bl.append(i)
   elif s[i]=='G' and i%2==1:
    gl.append(i)
  c=0
  for i in range(len(bl)):
   if t==0:
    c+=1
   else:
    c+=abs(gl[i]-bl[i])
  print(c)
 elif (b-g)>0:
  gl = []
  bl = []
  for i in range(len(s)):
   if s[i]=='B' and i%2==1:
    bl.append(i)
   elif s[i]=='G' and i%2==0:
    gl.append(i)
  c=0
  for i in range(len(bl)):
   if t==0:
    c+=1
   else:
    c+=abs(gl[i]-bl[i])
  print(c)
 else:
  gl = []
  bl = []
  for i in range(len(s)):
   if s[i]=='B' and i%2==0:
    bl.append(i)
   elif s[i]=='G' and i%2==1:
    gl.append(i)
  c1=0
  for i in range(len(bl)):
   if t==0:
    c1+=1
   else:
    c1+=abs(gl[i]-bl[i])
  gl = []
  bl = []
  for i in range(len(s)):
   if s[i]=='B' and i%2==1:
    bl.append(i)
   elif s[i]=='G' and i%2==0:
    gl.append(i)
  c2=0
  for i in range(len(bl)):
   if t==0:
    c2+=1
   else:
    c2+=abs(gl[i]-bl[i])
  if c2<c1:
   print(c2)
  else:
   print(c1)
