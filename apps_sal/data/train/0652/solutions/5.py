cases = int(input())
for i in range(0, cases):
 s1 = input()
 s2 = input()
 counter = 0
 s1 = s1.lower()
 s2 = s2.lower()
 for i in range(0, len(s1)):
  if s1[i] < s2[i]:
   print('first')
   break
  elif s1[i] > s2[i]:
   print('second')
   break
  else:
   counter += 1
 if counter == len(s1):
  print('equal')
