for _ in range(int(input())):
    N = int(input())
    array = list(map(int, input().split()))
    if N % 2 != 0:
        print('NO')
    else:
        possible = True
        p = N // 2
        for i in range(p):
            if array[i] == -1:
                if array[p + i] == -1:
                    array[i] = 1
                    array[p + i] = 1
                else:
                    array[i] = array[p + i]
            elif array[p + i] == -1:
                array[p + i] = array[i]
            elif array[i] != array[p + i]:
                possible = False
                break
        if possible:
            print('YES')
            print(*array)
        else:
            print('NO')
