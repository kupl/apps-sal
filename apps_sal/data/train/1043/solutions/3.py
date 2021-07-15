# cook your dish here
t = int(input())
for i in range(t):
 N, K = map(int, input().split())
 dict = list(map(str, input().split()))
 mod_pharse = []
 for m in range(K):
  l = list(map(str, input().split()))
  mod_pharse.extend(l[1:])

 for i in dict:

  if i in mod_pharse:

   print('YES', end=' ')
  else:
   print('NO', end=' ')
 print()

