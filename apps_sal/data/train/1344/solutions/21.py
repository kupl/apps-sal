def smallest(lst, n):
    if n == 2:
        print(lst[0] + lst[1])
    elif 2 < n <= 10:
        mini = lst[0] + lst[1]
        for j in range(2, n):
            suM = lst[j - 1] + lst[j]
            if suM < mini:
                mini = suM
        print(mini)


def __starting_point():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(i) for i in input().split()]
        smallest(arr, n)


__starting_point()
