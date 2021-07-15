# cook your dish here
for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 l=[]
 for i in range(n):
  for j in range(i+1,n):
    l.append(a[i]+a[j])
 print(l.count(max(l))/len(l))
