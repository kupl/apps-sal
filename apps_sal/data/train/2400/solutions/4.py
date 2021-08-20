from itertools import groupby


def go():
    n = int(input())
    x = list(map(int, input().split()))
    if all((xx == x[0] for xx in x)):
        return '1\n' + ' '.join(['1'] * n)
    if n % 2 == 0:
        return '2\n' + ' '.join(['1', '2'] * (n // 2))
    prev = x[-1]
    done = False
    ans = []
    cur = 0
    for xx in x:
        if prev == xx and (not done):
            done = True
        else:
            cur = (cur + 1) % 2
        ans.append(str(cur + 1))
        prev = xx
    if not done:
        ans[0] = '3'
        v = '3'
    else:
        v = '2'
    return v + '\n' + ' '.join(ans)


t = int(input())
ans = []
for _ in range(t):
    ans.append(str(go()))
print('\n'.join(ans))
