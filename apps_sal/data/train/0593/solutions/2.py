t=int(input())
n="abcdefghijklmnopqrstuvwxyz"
for i in range(t):
 m=0
 p=input().split()
 q=input()
 for j in range(len(n)):
  if(n[j] not in q):
   m=m+int(p[j])
 print(m)
