for _ in range(int(input())):
 prices = list(map(int,input().split(' ')))
 s = set(input())
 total = 0
 for x in range(97,123):
  ch = chr(x)
  if ch not in s:
   total += prices[ord(ch)-97]
 print(total)

