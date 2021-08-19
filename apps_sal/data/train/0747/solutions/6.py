# cook your dish here
def solve(n, lst):
    d = dict()

    p1 = []
    p2 = []
    for i in lst:
        if i in list(d.keys()):
            d[i] += 1
            p2.append(i)
            if d[i] > 2:
                return -1
        else:
            p1.append(i)
            d[i] = 1
    if d[max(p1)] > 1:
        return -1
    p1.sort()
    p2.sort()
    p2.reverse()
    return p1 + p2


t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split(' ')))
    res = solve(n, lst)
    if res == -1:
        print('NO')
    else:
        print('YES' + '\n' + ' '.join(map(str, res)))
