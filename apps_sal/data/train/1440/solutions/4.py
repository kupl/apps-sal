for i in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 a.sort()
 print(max(a[0]%a[n-1],a[n-1]%a[0]))
