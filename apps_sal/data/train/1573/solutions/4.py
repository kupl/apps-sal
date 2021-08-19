try:
    n = int(input())
    for _ in range(n):
        case = int(input())
        if case % 2 == 0:
            print('NO')
        else:
            print('YES')
            for i in range(case // 2 + 1):
                arr = [0] * case
                for j in range(i + 1, case // 2 + i + 1):
                    arr[j] = 1
                print(*arr, sep='')
            for i in range(case // 2):
                arr = [0] * case
                for j in range(i + 1):
                    arr[j] = 1
                for k in range(1, case // 2 - i):
                    arr[-k] = 1
                print(*arr, sep='')
except EOFError:
    pass
