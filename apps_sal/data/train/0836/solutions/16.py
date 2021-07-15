t = int(input())
while t:
 n = int(input())
 l = list(map(int, input().split()))
 r = list(map(int, input().split()))
 i = 0
 m = 1
 LR = [0,0]
 I = 0
 while i<n:
  if l[i] * r[i] > m:
   m = l[i] * r[i]
   LR = [l[i],r[i]]
   I = i
  elif LR[1] < r[i] and l[i] * r[i] == m:
   m = l[i] * r[i]
   LR = [l[i],r[i]]
   I = i
  i += 1
 print(I+1)
 t -= 1
  


