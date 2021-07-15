N,M=list(map(int,input().split()))
a=list(map(int,input().split()))
d=dict()
f,o=[],[]
for i in range(M):
 st=input().split()
 d[int(st[1])]=[st[2],int(st[0])]
 
for i in d:
 if d[i][1] in a:
  f.append(i)
 elif d[i][1] not in a:
  o.append(i)

f.sort()
o.sort()
for i in f[::-1]:
 print(d[i][0])
for j in o[::-1]:
 print(d[j][0])
