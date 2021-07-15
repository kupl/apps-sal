for _ in range(int(input())):
 n = int(input())

 cnt = 0
 for _ in range(n):
  s, j = map(int, input().split())

  if j - s > 5:   cnt += 1

 print(cnt)
