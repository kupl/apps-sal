from bisect import bisect_left,bisect_right
import string 

dic = {c:[] for c in string.ascii_lowercase}

n = int(input())
s = list(input())
q = int(input())

for i,c in enumerate(s,start=1):
  dic[c].append(i)
  
for i in range(q):
  p,l,r = map(str,input().split())
  if p =='1':
    j = int(l)
    if r == s[j-1]:
      continue
    c = s[j-1]    
    dic[c].pop(bisect_left(dic[c],j))
    dic[r].insert(bisect_left(dic[r],j),j)
    s[j-1] = r
  else:
    ans = 0
    l = int(l)
    r = int(r)
    for c in string.ascii_lowercase:
      pl = bisect_left(dic[c],l)
      if pl < len(dic[c]):
        if dic[c][pl] <= r:
          ans += 1
    print(ans)
