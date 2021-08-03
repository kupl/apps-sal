import sys
T = int(sys.stdin.readline().strip())
for t in range(T):
    sys.stdin.readline().strip()
    st = '0' + sys.stdin.readline().strip() + '0'
    res = 0
    for i in range(1, len(st) - 1):
        if st[i] == st[i - 1] == st[i + 1] == '0':
            res += 1
    print(res)
