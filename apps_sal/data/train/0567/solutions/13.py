t = int(input())
while t:
    n = input()
    l = list(map(int, input().split()))
    i = 0
    z = 1
    while i < len(l) - 2:
        if len(set(l[i:i + 3])) == 1:
            z = 0
            break
        else:
            i += 1
    if z == 0:
        print('Yes')
    else:
        print('No')
    t -= 1
