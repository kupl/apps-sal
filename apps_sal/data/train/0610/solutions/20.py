import sys
cases = int(sys.stdin.readline().rstrip())
for case in range(cases):
    N = int(sys.stdin.readline().rstrip())
    p = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    idxs = []
    for (i, v) in enumerate(p):
        if(v == 1):
            idxs.append(i)
    error = False
    for i in range(len(idxs) - 1):
        if idxs[i + 1] - idxs[i] < 6:
            error = True
            break
    if(error):
        print("NO")
    else:
        print("YES")
