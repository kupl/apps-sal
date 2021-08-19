t = int(input())
for i in range(t):
    n = int(input())
    dir = []
    for j in range(n):
        dir.append(input().strip().split())
    for j in range(n - 1):
        if dir[j + 1][0] == 'Right':
            dir[j][0] = 'Left'
        else:
            dir[j][0] = 'Right'
    dir[n - 1][0] = 'Begin'
    for j in reversed(dir):
        print(' '.join(j))
