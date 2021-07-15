for _ in range(int(input())):
 a = input().split()
 n = int(a[0])
 u = int(a[1])
 d = int(a[2])
 h = list(map(int, input().split()))
 parachute = True
 curr = 1
 for i in range(n-1):
  if h[i+1] > h[i]:
   if h[i+1] > h[i]+u:
    break
  elif h[i+1] < h[i]:
   if h[i+1] < h[i]-d:
    if parachute:
     parachute = False
    else:
     break
  curr += 1
 print(curr)
