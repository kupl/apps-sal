from sys import stdin

n = int(stdin.readline())

p = [int(x)-1 for x in stdin.readline().split()]

visited = [False for x in range(n)]

loops = []

for x in range(n):
    if not visited[x]:
        visited[x] = True
        start = x
        l = [x]
        cur = p[x]
        while cur != start:
            visited[cur] = True
            l.append(cur)
            cur = p[cur]
        loops.append(len(l)-1)


tot = sum(loops)

if n % 2 == 1:
    if tot % 2 == 1:
        print('Petr')
    else:
        print('Um_nik')
else:
    if tot % 2 == 0:
        print('Petr')
    else:
        print('Um_nik')

