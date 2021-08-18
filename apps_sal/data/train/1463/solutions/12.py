for _ in range(int(input())):

    n = int(input())
    if n <= 3:
        print(1)
        ans = []
        for i in range(n):
            ans.append(i + 1)
        print(n, *ans)

    else:
        print(n // 2)
        if n % 2 == 0:
            for i in range(1, n + 1, 2):
                print(2, i, i + 1)
        else:
            print(3, 1, 2, 3)
            for i in range(4, n + 1, 2):
                print(2, i, i + 1)
