for _ in range(int(input())):
    int_num = list(map(int, input().split()))
    (a, b, c) = sorted(int_num)
    if a + b <= c or a + c <= b or b + c <= a or (c <= a or c <= b):
        print('NO')
    elif a ** 2 + b ** 2 == c ** 2:
        print('YES')
    else:
        print('NO')
