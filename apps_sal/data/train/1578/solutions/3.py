# your code goes here
t = int(input())
for _t in range(t):
 st = input()
 ans = 0
 for i in st:
  if i>'0' and i <= '9':
   ans += int(i)
 print(ans)
