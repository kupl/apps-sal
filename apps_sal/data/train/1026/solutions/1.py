# cook your dish here
for _ in range(int(input())):
 a=[int(x) for x in input().split()]
 a.sort()
 m=(10**9+7)
 print((a[0]*(a[1]-1)*(a[2]-2))%m)
