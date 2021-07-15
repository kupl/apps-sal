s=list(input())
n=len(s)
if s[0] != "1" or s[-1]=="1" or s[:(n-1)//2] != s[n-2:n//2-1:-1]:
  print(-1)
  return
chain = [1]
ans = []
s[-1] = "1"
for i in range(1,n):
  if s[i] == "1":
    chain.append(i+1)
    ans.append((chain[-2],chain[-1]))
c = len(chain)
for i in range(1,c):
  for j in range(chain[i-1]+1,chain[i]):
    ans.append((j,chain[i]))
for edge in ans:
  print(*edge)
