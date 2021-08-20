def smallest(lst, n):
    if n == 2:
        print(lst[0] + lst[1])
    else:
        mini = lst[0] + lst[1]
        for j in range(1, n):
            for k in range(j + 1, n):
                s = lst[j] + lst[k]
                if s < mini:
                    mini = s
        print(mini)


def __starting_point():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(i) for i in input().split()]
        smallest(arr, n)


__starting_point()
