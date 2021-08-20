"""stdin=open('input.txt')
def input():
    return stdin.readline()[:-1]
"""
(p, s) = input().split()
p = int(p)
s = int(s)
n = [0 for i in range(p)]
for prob in range(p):
    points = list(map(int, input().split()))
    nop = list(map(int, input().split()))
    for i in range(s):
        nop[i] = [points[i], nop[i]]
    nop.sort()
    for i in range(s - 1):
        if nop[i][1] > nop[i + 1][1]:
            n[prob] += 1
for i in range(p):
    n[i] = [n[i], i]
n.sort()
for i in range(p):
    print(n[i][1] + 1)
