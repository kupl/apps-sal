# cook your dish here
for _ in range(0,int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 a=[]
 for i in range(0,n):
  a.append(i+l[i])
 a.sort(reverse=True)
 print(a[0])
