for _ in range(int(input())):
    length = int(input())
    S = input()
    R = input()
    if S.count('1') == R.count('1'):
        print('YES')
    else:
        print('NO')
