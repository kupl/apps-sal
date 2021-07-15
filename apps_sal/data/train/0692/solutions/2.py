n = eval(input())
arr = list(map(int,input().split()))
q = eval(input())
while q:
 q -= 1
 ar = input().split()
 t = ar[0]
 l = int(ar[1])
 r = int(ar[2])
 l -= 1
 if t == 'U':
  arr[l] = r
 elif t == 'A':
  print(sum(arr[l:r]))
 elif t == 'M':
  print(max(arr[l:r]))
 elif t == 'm':
  print(min(arr[l:r]))
 elif t == 'S':
  m = max(arr[l:r])
  m2 = -1
  for i in range(l, r):
   if arr[i] < m and arr[i] > m2:
    m2 = arr[i]
  print(m2)
 elif t == 's':
  m = min(arr[l:r])
  m2 = 1000000000000
  for i in range(l, r):
   if arr[i] > m and arr[i] < m2:
    m2 = arr[i]
  print(m2)
 

