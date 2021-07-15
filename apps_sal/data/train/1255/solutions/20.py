# cook your dish here
for _ in range(int(input())):
 s,k = input().split()
 k = int(k)
 ref = "abcdefghijklmnopqrstuvwxyz"
 l = len(s)
 r = ""
 i=0
 while len(r)!=l and i<26:
  if ref[i] in s and k>0:
   r+=ref[i]
   i+=1
   k-=1
  elif ref[i] in s:
   i+=1
   continue
  else:
   r+=ref[i]
   i+=1
 if len(r) == len(s):
  print(r)
 else:
  print("NOPE")
   

