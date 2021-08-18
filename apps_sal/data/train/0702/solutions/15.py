for _ in range(int(input())):
    m, a, b = map(int, input().split())
    mins = abs(a - b) // 3
    step = abs(a - b) % 3
    if(step == 0):
        if(mins <= m):
            print('No')
        else:
            print('Yes')
    else:
        print('Yes')
