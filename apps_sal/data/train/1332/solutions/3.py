n = eval(input())
n = int(n)
i = 0
while i<n:
 i+=1
 def path(fr, to):
  if fr < to:
   fr, to = to, fr
   
  if fr == to:
   return 0
  
  elif fr == 1:
   return path(to, 1)
  
  elif fr%2:
   up = int((fr-1)/2)
   return 1 + path(up, to)
  
  elif not fr%2:
   up = int(fr/2)
   return 1 + path(up, to)
  
 cor = input().split()
 f = int(cor[0])
 t = int(cor[1])
 
 print(path(f,t))

