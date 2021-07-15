# cook your dish here
for h in range(int(input())):
 n = int(input())
 a = list(map(int,input().split()))
 a.sort()
 x = a[(n//4)]
 y = a[(n//2)]
 z = a[(3*n//4)]
 if x==a[n//4-1] or y==a[n//2-1] or z==a[3*n//4-1]:
  print(-1)
 else:
  print(x,y,z)
