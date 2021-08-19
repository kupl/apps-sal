for _ in range(int(input())):
    s = input().split('W')
    if len(s[1]) == len(s[0]):
        print('Chef')
    else:
        print('Aleksa')
