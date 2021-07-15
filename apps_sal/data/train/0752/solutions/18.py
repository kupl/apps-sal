N,Q = map(int,input().split())

types={}

for _ in range(N):
 K,V=input().split()
 types[K]=V

for _ in range(Q):
 fileName = input().strip()
 I = fileName.rfind('.')
 if(I != -1):
  extension = fileName[I+1:]
  if(extension in types.keys()):
   print(types[extension])
  else:
   print('unknown')
 else:
  print('unknown')
