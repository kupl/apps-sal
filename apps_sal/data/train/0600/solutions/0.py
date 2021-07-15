import math

t = int(input())

a = [-1, 0, 1]

for i in range(58):
 temp = a[-1] + a[-2]
 temp = temp%10
 a.append(temp)
 
for _ in range(t):
 n = int(input())
 
 temp = len(bin(n)) - 3
 temp = 2**temp
 temp = temp%60
 
 print(a[temp])
