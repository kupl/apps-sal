n = int(input())

a = [0] * n
for i in range(n):
    a[i] = list(map(int, input().split()))
unused = set(range(1, n + 1))
used = {0}
bind = [-1] * (n)
for cur in range(1, n + 1):
    for i in range(n):
        if (bind[i] == -1) and (max(a[i]) <= cur):
            bind[i] = cur
            break
print(' '.join(map(str, bind)))
