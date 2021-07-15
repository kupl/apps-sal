n=int(input().split()[0])
s=input().split()
l=[0 for i in range(n)]
m=[0 for i in range(n)]
M=[0 for i in range(n)]
for i in range(n):
  l[i]=int(s[i])
m[0]=l[0]
M[0]=l[-1]
for i in range(1,n):
  m[i]=min(m[i-1],l[i])
  M[i]=max(M[i-1],l[-i-1])
M.reverse()
d=[M[i]-m[i] for i in range(n)]
ma=max(d)
memo=-1
cnt=0
for i in range(n):
   if d[i]==ma and m[i]!=memo:
      cnt+=1
      memo=m[i]
print(cnt)
