for _ in range(int(input())):
    n = input()
    if len(n) >= 4:
        if n[-4:] == '1000':
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
