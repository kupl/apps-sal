for _ in range(int(input())):
    st = input().split('W')
    if len(st[1]) == len(st[0]):
        print('Chef')
    else:
        print('Aleksa')
