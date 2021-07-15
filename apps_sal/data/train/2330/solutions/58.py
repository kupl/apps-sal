s=input()
n=len(s)
if s[0]=="0" or s[-1]=="1":print(-1);return
for i in range(n-1):
  if s[i]!=s[-i-2]:print(-1);return
b=[]
for i in range(n-1):
  if s[i]=="1":
    for j in b:print(j+1,i+1)
    b=[]
  b.append(i)
for j in b:print(j+1,n)
