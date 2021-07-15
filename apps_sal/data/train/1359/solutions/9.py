# cook your dish here
for _ in range(int(input())):
 N = int(input())
 array = list(map(int, input().split()))
 odds = 0
 even = 0
 for i in array:
  if i % 2 == 0:
   even += 1
  else:
   odds += 1

 if (even > 1):
  ans = odds + (even - 1) * 2
 else:
  ans = odds
 if odds > 1:
  ans = min(ans, even + (odds - 1) * 2)
 else:
  ans = min(ans, even)
 print(ans)
