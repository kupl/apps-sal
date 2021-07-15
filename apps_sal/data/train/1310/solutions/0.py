t = int(input())
for tc in range(t):
 seq = input()
 dollar = 0
 stamp = 0
 for ct in seq:
  if stamp >= 6:
   stamp -= 6
   continue
  elif ct == 'M':
   dollar += 3
  elif ct == 'L':
   dollar += 4
  stamp += 1
 print(dollar)



