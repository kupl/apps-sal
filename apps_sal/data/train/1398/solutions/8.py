try:
 t = int(input())
 for w in range(t):
  s = str(input())
  k = list(s)
  q = []
  for i in range(0,len(k)):
   if (k[i] in k):
    if (k[i] not in q):
     q.append(k[i])
  
  print(len(q)) 
 
except EOFError as e:
 pass
