for _ in range(int(input())):
 n, k = [int(i) for i in input().split()]
 s = input().split()
 for i in range(k):
  if s.pop() == 'H':
   for ind, j in enumerate(s):
    if j == 'H':
     s[ind] = 'T'
    else:
     s[ind] = 'H'
 print(sum([1 for i in s if i =='H']))
