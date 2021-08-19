import sys
T = int(sys.stdin.readline().strip())
for t in range(T):
    n = int(sys.stdin.readline().strip())
    arr = []
    for i in range(n):
        tmp = sys.stdin.readline().strip()
        arr.append(list(tmp))
    can = True
    for i in range(n - 1):
        for j in range(n - 1):
            if arr[i][j] == '1':
                if arr[i + 1][j] == '0' and arr[i][j + 1] == '0':
                    can = False
                    break
        if not can:
            break
    if can:
        print('YES')
    else:
        print('NO')
