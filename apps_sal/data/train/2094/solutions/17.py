n = int(input())
s = input()
z = s.count('z')
e = s.count('e')
r = s.count('r')
o = s.count('o')
n = s.count('n')
ones = min(o, n, e)
o -= ones
n -= ones
e -= ones
zeros = min(z, e, r, o)
res = []
res += [1] * ones
res += [0] * zeros
print(*res)
