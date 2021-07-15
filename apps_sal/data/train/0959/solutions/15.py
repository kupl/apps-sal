for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 a.sort()
 s=0
 for i in range(n//2):
  s+=abs(a[n-i-1]-a[i])
 print(s) 
