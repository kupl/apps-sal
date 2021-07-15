import math
t = int(input())
while t:
 n = int(input())
 c = 0
 i = (1 + math.ceil((9 + 8 * n)**0.5) - 1) // 2
 # print(i)
 c = (i * (i + 1) // 2) - 1
 # print(c)
 print(int(i - (c - n) - 1))
 t-=1
