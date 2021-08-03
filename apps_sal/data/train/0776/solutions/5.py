for _ in range(int(input())):
    n = int(input())
    a = n // 99998
    b = n % 99998
    print(3 * (a + 1))
    print(f'1 99999 100000 ' * a + f'1 {b+1} {b+2}')
