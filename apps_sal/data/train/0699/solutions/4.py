for i in range(int(input())):
 n,k,d = map(int, input().split())
 l = list(map(int,input().split()))
 t = sum(l)
 if t < k :
  print("0")
 elif t == k:
  print("1")
 elif t>k:
  a = t//k
  if a >= d:
   print(str(d))
  else:
   print(str(a))
