q = int(input())
for i in range(q):
    s = list(input()) + ['R']
    ans = 0
    cur = 0
    for x in s:
        if x == 'L': cur += 1
        else:
            if ans < cur: ans = cur
            cur = 0
    print(ans + 1)
