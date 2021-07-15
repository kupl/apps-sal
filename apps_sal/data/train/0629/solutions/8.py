t = int(input()) 
for i in range (t) :
 line = input()
 pui = line.split()
 r = int(pui[0])
 g = int(pui[1]) 
 b = int(pui[2]) 
 m = int(pui[3]) 
 ar = list()
 for i in range (3) :
  line = input()
  pui = line.split()
  pui = [int (j) for j in pui]
  ar.append(pui) 
 for i in range (m) :
  R = max(ar[0]) 
  G = max(ar[1]) 
  B = max(ar[2]) 
  if R>=G and R >= B :
   for j in range(len(ar[0]))  :
    ar[0][j] = int(ar[0][j] / 2) 
  elif G >= R and G >= B :
   for j in range(len(ar[1])) : 
    ar[1][j] = int(ar[1][j] / 2) 
  elif B >= G and B >= R :
   for j in range(len(ar[2])) : 
    ar[2][j] = int(ar[2][j] / 2)
 R = max(ar[0]) 
 G = max(ar[1]) 
 B = max(ar[2])
 ans = max(R, G, B)
 print(ans)

