'''t=int(input())
for _ in range(t):
    l=[0]
    r=[1]
    p,idx=map(int,input().split())
    for i in range(1,p):
     for j in range(1,pow(i,2)+1,2):
      l.append(pow(2,p-i)*j)
    for i in range(1,p):
     for j in range(1,pow(i,2)+1,2):
      r.append(pow(2,p-i)*j+1)
    l.extend(r)
    print(l)
    print(l[idx])'''
try:
 t=int(input())
 for _ in range(t):
  p,idx=map(int,input().split())
  print(int(bin(idx)[2:].zfill(p)[::-1],2))
except:
 pass
