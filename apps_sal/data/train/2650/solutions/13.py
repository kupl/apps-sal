a,b=map(int,input().split())
s=[]
for i in range(a):
  s.append(input())
s.sort()
for i in range(a):
  print(s[i],end="")
