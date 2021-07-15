# cook your dish here
t=int(input())
while(t>0):
 fs,k=map(str,input().split())
 k=int(k)
 fs=list(set(fs))
 arr=""
 for a in range(97,123):
  if(chr(a) in fs):
   if(k>0):
    arr+=chr(a)
    k-=1
   else:
    continue
  else:
   arr+=chr(a)
 if(len(fs)<=len(arr)):
  print(arr[:len(fs)])
 else:
  print('NOPE')
 t-=1
