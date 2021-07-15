T = int(input())
for i in range(T):
 n = int(input())
 S = input()
 R = input()
 l = [x for x in S]
 m = [x for x in R]
 if ((l.count('0') == m.count('0')) or (l.count('1') == m.count('1'))):
  print("YES")
 else:
  print("NO")
