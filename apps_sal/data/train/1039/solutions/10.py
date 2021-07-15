test_case = int(input())

while test_case > 0:
 x, y = list(map(int, input().split(' ')))
 difference = abs(x - y)
 ans = 0
 if x > y:
  if difference % 2 == 0:
   ans = 1
  else:
   ans = 2
 elif x < y:
  if difference % 2 == 0 and difference % 4 != 0:
   ans = 2
  elif difference % 2 == 1:
   ans = 1
  else:
   ans = 3
 elif x == y:
  ans = 0
 print(ans)
 test_case -= 1

