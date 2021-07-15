from collections import defaultdict
n = int(input())

home = input()
d = defaultdict(int)

for i in range(n):
    s = input()
    fr, to = s.split('->')
    d[fr] -= 1
    d[to] += 1

if d[home] == 0:
    print('home')
else:
    print('contest')

