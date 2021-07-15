m = 10**9+7
n = 10**6

h = 1
b = [0]*n
c = [0]*n

for i in range(1,n+1):
 h *= i
 h %= m
 b[i-1] = h%m
h=1
for i in range(n):
 h *= b[i]
 h %= m
 c[i] = h%m
for z in range(int(input())):
 print(c[int(input())-1])
