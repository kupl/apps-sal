for _ in range(int(input())) :
 n = int(input())
 a = list(map(int, input().split()))
 a.sort()
 sum = 0
 for i in range(n//2) :
  sum += (a[n-i-1] - a[i])
 print(sum)
