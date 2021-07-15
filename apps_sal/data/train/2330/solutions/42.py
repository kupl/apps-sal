s=input()
if s[0]=="0":print(-1);return()
if s[-1]=="1":print(-1);return()
for i in range(len(s)-1):
  if s[i]!=s[(len(s)-1)-(i+1)]:print(-1);return()
ans=[]
for i in range(len(s)-1):
  if s[i]=="1":
    for j in ans:print(j+1,i+1)
    ans=[]
  ans.append(i)
for j in ans:print(j+1,len(s))
