t = int(input())
g = 'abcdefghijklmnopqrstuvwxyz'
while t:
 t-=1
 s,k = input().split()
 h = len(s)
 k = int(k)
 ans = []
 count = 0
 d = {}
 for i in s:
  d[i] = True
 s = list(s)
 s = sorted(s)
 for i in range(k):
  ans.append(s[i])
 currentIndex=0
 ans = ans[::-1]
 for i in range(26):
  if g[i] not in d:
   if count+k<h:
    count+=1
    ans.append(g[i])
    ans = sorted(ans)[::-1]
   else:
    for j in range(h):
     if ans[j]>g[i]:
      ans[j] = g[i]
      ans = sorted(ans)[::-1]
      break
 ans = sorted(ans)
 if count+k == h:
  
  print(''.join(ans))
 else:
  print("NOPE")

