for _ in range(int(input())):
    n = int(input())
    a = n - 1
    su = n ** 2 * (n + 1) ** 2 // 4
    tu = a ** 2 * (a + 1) ** 2 // 4
    print(su + tu)
