for _ in range(int(input())):
    x = set(input())
    y = set(input())
    if(len(x & y)):
        print('Yes')
    else:
        print('No')
