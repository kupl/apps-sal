def checkAccending(li):
    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    b = sorted((int(i) for i in input().split()))
    g = sorted((int(i) for i in input().split()))
    sb = []
    sg = []
    for i in range(n):
        sb.append(b[i])
        sb.append(g[i])
        sg.append(g[i])
        sg.append(b[i])
    if checkAccending(sb) or checkAccending(sg):
        print('YES')
    else:
        print('NO')
