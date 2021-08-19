for _ in range(int(input())):
    s = input()
    if len(s) < 4:
        print('NO')
    elif s[-4:] == '1000':
        print('YES')
    else:
        print('NO')
