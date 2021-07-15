T = int(input())
while(T > 0):
 n = int(input())
 l = list(map(int, input().split()))
 s = list(sorted(set(l)))
 maxx = 0
 ans = 0
 for i in s:
  curr = 0
  j = 0
  while(j < n):
   if(l[j] == i):
    curr += 1
    j += 2
   else:
    j += 1
  if(curr > maxx):
   maxx = curr
   ans = i
 print(ans)
 T -= 1
