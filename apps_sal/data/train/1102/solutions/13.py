t = int(input())

for _ in range(t):
 n = input().strip()
 answer = 1
 for x in n:
  if int(x) <= 6 or int(x) == 8:
   answer *= 3
  elif int(x) == 7 or int(x) == 9:
   answer *= 4
 print(answer % 1000000007)

