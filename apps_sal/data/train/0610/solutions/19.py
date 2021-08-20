for _ in range(int(input())):
    n = int(input())
    a = input()
    if '1 1' in a or '1 0 1' in a or '1 0 0 1' in a or ('1 0 0 0 1' in a) or ('1 0 0 0 0 1' in a):
        print('NO')
    else:
        print('YES')
