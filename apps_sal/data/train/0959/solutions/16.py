for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 a.sort()
 c=0
 for i in range(n//2):
  c+=abs(a[i]-a[-i-1])
 print(c)

