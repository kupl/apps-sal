for t in range(int(input())):

 N = int(input())
 ans = []
 st = None
 numb = 0
 num = None

 for i in range(1,N+1):

  if i % 2 and i == 1:
   ans.append(chr(65))
   st = chr(65)

  elif i % 2:
   ans.append(st + chr(65 +len(st)) + chr(65 + len(st) + 1))

   st += chr(65 +len(st))
   st += chr(65 + len(st))

  else:

   if not num:
    num = '12'
    ans.append(num)
    numb = 2

   else:
    num += str(numb + 1)
    num += str(numb + 2)

    ans.append(num)
    numb += 2


 for i in ans:

  print(' '*(N-1) + i)
  N -= 1


