for _ in range(int(input())):
 a = [0]*26
 s = input()
 t = s[::-1]
 for c in s:
  a[ord(c)-ord('a')]+=1
 l = []
 for i in range(26):
  if (a[i]==1):
   l.append(chr(ord('a')+i))
 if (len(l)<=1):
  print("PANDEY")
 else:
  shan = ""
  for c in s:
   if (c in l):
    shan = c
    break
  anku = ""
  for c in t:
   if (c in l):
    anku = c
    break
  if (shan>anku):
   print("SHANKY")
  else:
   print("ANKU")

