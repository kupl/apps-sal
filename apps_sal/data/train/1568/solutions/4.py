for _ in range(int(input())):
  c = 0
  n = int(input())
  a = list(map(int,input().split()))
  for i in range(len(a)):
    if a[i] >= n//2:
      c += 1
  print(c)

