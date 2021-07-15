n = int(input())
M = [[int(x) for x in input().split()] for i in range(n)]
last = False
perm = [0 for i in range(n)]
for i in range(n):
    S = set()
    for x in M[i]:
        if x in S:
            perm[i] = x
            break
        else:
            S.add(x)
    else:
        if last:
            perm[i] = n-1
        else:
            perm[i] = n
            last = True
for x in perm:
    print(x, end = ' ')

