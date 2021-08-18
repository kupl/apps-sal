import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    c = list(map(int, sys.stdin.readline().split()))
    v = 0
    for j in range(n - 2):
        if c[j] == c[j + 1] == c[j + 2]:
            v += 1
            break
        else:
            pass
    if v == 1:
        sys.stdout.write('Yes\n')
    else:
        sys.stdout.write('No\n')
