for _ in range(int(input())):
 s,k=input().split()
 k=int(k)
 # arr = list(n)
 t=""
 for i in range(97,123):
  if chr(i) not in s:
   t+=chr(i)
   if len(t)==len(s):
    break
  elif chr(i) in s and k>0:
   t+=chr(i)
   k-=1
   if len(t)==len(s):
    break
 if len(t)==len(s):
  print(t)
 else:
  print("NOPE")

