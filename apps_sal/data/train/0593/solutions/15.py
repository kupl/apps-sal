T = int(input())
for i in range(T):
 s = input()+' '
 cost = {}
 present = {}
 spend = 0
 for j in range(26):
  n = s.find(' ')
  cost[97+j] = int(s[:n])
  present[97+j] = False
  s = s[n+1:]
 s = input()
 for k in range(len(s)):
  t = ord(s[k])
  present[t] = True
 for l in range(26):
  if present[97+l] == False:
   spend += cost[97+l]
 print(spend)
