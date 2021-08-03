import sys
input = sys.stdin.readline

n = int(input())
com = []

for _ in range(n):
    l = input().split()
    com.append((l[0], int(l[1])))

AND, OR, XOR = [], [], []

for i in range(10):
    res1 = 0
    res2 = 1

    for s, n in com:
        b = (n >> i) & 1

        if s == '&':
            res1 &= b
            res2 &= b
        elif s == '|':
            res1 |= b
            res2 |= b
        elif s == '^':
            res1 ^= b
            res2 ^= b

    if (res1, res2) == (0, 0):
        AND.append(i)
    elif (res1, res2) == (1, 1):
        OR.append(i)
    elif (res1, res2) == (1, 0):
        XOR.append(i)

AND_n = 0

for i in range(10):
    if i not in AND:
        AND_n += 2**i

OR_n = 0

for i in OR:
    OR_n += 2**i

XOR_n = 0

for i in XOR:
    XOR_n += 2**i

print(3)
print('&', AND_n)
print('|', OR_n)
print('^', XOR_n)

"""
for i in range(1024):
    res1 = i
    
    for s, n in com:
        if s=='&':
            res1 &= n
        elif s=='|':
            res1 |= n
        elif s=='^':
            res1 ^= n
    
    res2 = i
    res2 &= AND_n
    res2 |= OR_n
    res2 ^= XOR_n
    
    if res1!=res2:
        1/0
"""
