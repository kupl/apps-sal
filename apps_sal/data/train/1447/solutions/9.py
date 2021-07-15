a = int(input())
for i in range(0, a):
 b = int(input())
 c = list(map(int, input().split()))
 n = [0 for k in range(0, 1000)]
 f1 = [0 for k in range(0, 1000)]
 f2 = [0 for k in range(0, 1000)]
 for l in range(0, b):
  f1[c[l] - 1] += 1
 bo = True
 for l in range(0, 1000):
  if(f1[l] > 0):
   f2[f1[l]] += 1
   if(f2[f1[l]] > 1):
    bo = False
    break
 if(bo):
  j = 1
  n[c[0] - 1] = 1
  while(j < b):
   if(c[j] == c[j-1]):
    j += 1
   elif(c[j] != c[j - 1] and n[c[j] - 1] != 1):
    n[c[j] - 1] = 1
    j+= 1
   else:
    print("NO")
    break
  if(j == b):
   print("YES")
 else:
  print("NO")

