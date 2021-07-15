import string
t= int (input().strip())
for i in range(t):
 s=input().strip()
 c=0
 for j in s:
  if j.isdigit():
   c+=int(j)
 print(c)

