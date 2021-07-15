for t in range(int(input())):
 s = input()
 r = input()
 diff = list()
 index = list()
 cnt = 0
 for i in range(len(s)):
  if s[i] != r[i]:
   cnt += 1
   index.append(i)
 for i in range(1, len(index)):
  diff.append(index[i] - index[i - 1] - 1)
 diff.sort()
 fmin = cnt ** 2
 oper = cnt ; moves = cnt
 for i in diff:
  moves += i
  oper -= 1
  fmin = min(fmin, moves * oper)
 print(fmin)
