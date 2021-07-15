t = int(input())
for _ in range(t):
 s = input()
 a = ["A","B","C","D","E","F","G","H","I","J"]
 enemy = 0
 for i in range(len(s)):
  if s[i] in a:
   enemy += 1
 print(enemy)
