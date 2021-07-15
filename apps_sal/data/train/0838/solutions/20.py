t = int(input())
for _ in range(t):
 n = int(input())
 wlist = list(map(int, input().split()))
 maxi = 0
 for j in range(0,n):
  if wlist[j] + j > maxi:
   maxi = wlist[j] + j
 print(maxi)

