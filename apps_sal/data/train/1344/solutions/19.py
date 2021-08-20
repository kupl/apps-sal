def smallest(lst, n):
    if n == 2:
        print(lst[0] + lst[1])
    else:
        reslst = []
        mini = lst[0] + lst[1]
        for j in lst:
            for k in lst:
                if lst.index(j) == lst.index(k):
                    continue
                s = j + k
                reslst.append(s)
        print(min(reslst))


def __starting_point():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(i) for i in input().split()]
        smallest(arr, n)


__starting_point()
