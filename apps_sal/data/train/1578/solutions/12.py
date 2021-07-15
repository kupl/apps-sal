T = int(input())
for t in range(T):
 word = input()
 s = 0
 for c in word:
  if c.isdigit():
   s += int(c)
 print(s)

