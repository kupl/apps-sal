# cook your dish here
t=int(input())
while(t):
 n=int(input())
 l=[]
 for i in range(n):
  l.append(list(map(int,input().split())));
 m=[]
 for i in l:
  m.append((i[1]//(i[0]+1))*i[2])
 res=max(m)
 print(res)
 t=t-1
