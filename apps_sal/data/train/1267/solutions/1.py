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
for _ in range(m):
 inp = [int(x) for x in input().split()]
 p += [inp]
max_row = []
for i in p:
 max_row += [max(i)]
ans = dfs(0,m,n,k)
w = []
for i in ans:
 cst = 0
 for j in range(m):
  if(p[j]!="z"):
   cst += p[j][ord(i[j])-97]
  else:
   cst += max_row[j]
 w += [(-cst,i)]
w.sort()
print(w[k-1][1])

