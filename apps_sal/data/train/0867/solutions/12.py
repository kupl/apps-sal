for _ in range(int(input())):
 s, a, b, c = list(map(int, input().split()))
 if s >= (a + b + c ):
  ans = 1
 elif s >= (a + b) or s >= (b +c):
  ans = 2
 else:
  ans = 3
 print(ans)
  

