n = int(input())
for _ in range(n):
 x, y = list(map(int, input().split()))
 bx = bin(x)[2:]
 by = bin(y)[2:]
 i = 0
 while i < min(len(bx), len(by)) and bx[i] == by[i]:
  i += 1
 print(len(bx)+len(by) - 2*i)

