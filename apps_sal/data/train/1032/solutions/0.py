a = [1]
M = 10**6 + 3
for ii in range(1, 1000005):
 a.append((a[-1]*ii)%M)
for __ in range(eval(input())):
 n, x = list(map(int, input().split()))
 if n>=M: print(0)
 else: print((a[n]*x)%M)

