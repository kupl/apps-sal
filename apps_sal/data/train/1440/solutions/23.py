for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 a.sort()
 s=a[0]
 for i in range(1,n):
  s=s%a[i]
 print(s) 
