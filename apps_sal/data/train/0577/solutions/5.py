s1 = input()
for i in range(int(input())):
 s2 = input()
 a= ''.join(sorted(s1))
 c= ''.join(set(s2))
 b= ''.join(sorted(c))
 if b in a:
  print('Yes')
 else:
  print('No')
