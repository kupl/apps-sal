for _ in range(int(input())):
 n,k = map(int,input().split())
 ans = 0
 for x in map(int, input().split()):
  if (x+k)%7 == 0: ans += 1
 print(ans)
