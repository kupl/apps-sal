t = int(input())
for i in range(t):
    s = input()
    if len(s) < 4:
        print('NO')
    elif s[-4:] != '1000':
        print('NO')
    else:
        print('YES')
