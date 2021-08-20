for i in range(int(input())):
    n = int(input())
    l = sum(list(map(int, input().split())))
    n = l / n
    if n.is_integer():
        print('Yes')
    else:
        print('No')
