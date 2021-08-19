t = int(input())
for i in range(t):
    n = int(input())
    x = int(input())
    exp = list(map(int, input().split()))
    exp.sort()
    while len(exp) >= x:
        if 1 in exp:
            break
        else:
            exp = exp[x:]
            exp = [e - 1 for e in exp]
    if 1 not in exp:
        print('Possible')
    else:
        print('Impossible')
