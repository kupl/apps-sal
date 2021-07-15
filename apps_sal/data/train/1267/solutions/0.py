def dfs(ind,m,n,k):
 if(ind == m):
  return [""]
 else:
  temp = dfs(ind+1,m,n,k)
  ans = []
  if(len(temp)<k):
   for i in temp:
    for j in range(97,97+n):
     ans += [chr(j)+i]
  else:
   for i in temp:
    ans += ["z"+i]
 return ans
n,m,k = list(map(int,input().split()))
p = []
mr= []
for _ in range(m):
 inp = [int(x) for x in input().split()]
 mc = inp[0]
 mi = 0
 for j in range(1,n):
  if(mc<inp[j]):
   mc = inp[j]
   mi = j
 p += [inp]
 mr += [mi]
ans = dfs(0,m,n,k)
w = []
for i in ans:
 cst = 0
 s = ""
 for j in range(m):
  if(i[j]!="z"):
   s+=i[j]
   cst += p[j][ord(i[j])-97]
  else:
   s += chr(mr[j]+97)
 w += [(-cst,s)]
w.sort()
print(w[k-1][1])

