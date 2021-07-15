# cook your dish here
rii = lambda : map(int, input().strip().split(" "))
ril = lambda : list(map(int, input().strip().split(" ")))
ri = lambda : int(input().strip())
rs = lambda : input()
T = ri()
for _ in range(T):
 N = ri()
 l1 = rs()
 l2 = rs()
 nb1_1 = len(list(filter(lambda x: x == '1', l1)))
 nb2_1 = len(list(filter(lambda x: x == '1', l2)))
 if nb1_1 == nb2_1:
  print("YES")
 else:
  print("NO")
