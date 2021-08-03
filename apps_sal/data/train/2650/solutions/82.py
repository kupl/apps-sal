
N, L = map(int, input().split())

l = []
for _ in range(N):
    s = input()
    l.append(s)

l.sort()

for i in l:
    print(i, end='')
