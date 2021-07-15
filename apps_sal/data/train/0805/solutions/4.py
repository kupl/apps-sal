# cook your dish here
for i in range(int(input())):
 n=int(input())
 l=[]
 for j in range(n):
  s,p,v = list(map(int, input().split()))
  l.append((p//(s+1))*v)
 print(max(l))


