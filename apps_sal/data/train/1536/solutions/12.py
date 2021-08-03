for _ in range(int(input())):
    N = int(input())
    array = list(map(int, input().split()))
    d1 = array[1] - array[0]
    d2 = array[2] - array[1]
    d3 = array[3] - array[2]
    d = 0
    if d1 == d2:
        d = d1
    elif d1 == d3:
        d = d1
    elif d2 == d3:
        d = d2
    else:
        d = (array[3] - array[0]) // 3

    for i in range(N - 1):
        if array[i + 1] - array[i] != d:
            if i == 0:
                if array[2] - array[1] == d:
                    array[0] = array[1] - d
                else:
                    array[1] = array[0] + d
            else:
                array[i + 1] = array[i] + d
            break
    print(*array)
