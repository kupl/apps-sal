for _ in range(int(input())):
    N = int(input())
    S = input()
    R = input()
    if S.count('0') == R.count('0'):
        print('YES')
    else:
        print('NO')
