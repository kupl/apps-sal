for _ in range(int(input())):
    a = set(list(input()))
    b = set(list(input()))
    if len(a & b) == 0:
        print('No')
    else:
        print('Yes')
