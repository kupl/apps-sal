for _ in range(int(input())) :
 n, k = map(int,input().split())
 k = 100-k
 a = list(map(int,input().strip().split()))
 b = list(map(int,input().strip().split()))
 d_min = 100
 a_min = 100
 for i in range(n) :
  if b[i] == 0 and a[i]<d_min :
   d_min = a[i]
  elif b[i] == 1 and a[i]<a_min :
   a_min = a[i]
 if a_min+d_min <= k :
  print("yes")
 else :
  print("no")
