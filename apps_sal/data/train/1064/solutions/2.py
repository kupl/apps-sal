# cook your dish here
for i in range(int(input())):
 s = list(input())
 for i in range(len(s)-4,-1,-1):
  c = 0
  if s[i] == "?":
   c+=1
  else:
   if s[i] == "C":
    c+=1
   else:
    continue
   
  if s[i+1] == "?":
   c+=1
  else:
   if s[i+1] == "H":
    c+=1
   else:
    continue
   
  if s[i+2] == "?":
   c+=1
  else:
   if s[i+2] == "E":
    c+=1
   else:
    continue
   
  if s[i+3] == "?":
   c+=1
  else:
   if s[i+3] == "F":
    c+=1
   else:
    continue
  if c == 4:
   s[i] = "C"
   s[i+1] = "H"
   s[i+2] = "E"
   s[i+3] = "F"
 for j in range(len(s)-1,-1,-1):
  if s[j] == "?":
   s[j] = "A"
 print(*s,sep="")

