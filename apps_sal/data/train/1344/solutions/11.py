for i in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))[:n]
 a.sort()
 print(a[0]+a[1])
