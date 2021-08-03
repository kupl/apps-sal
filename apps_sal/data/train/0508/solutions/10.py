from bisect import bisect_left


def main():
    ConstNum, PersonNum = map(int, input().split())

    S = []
    T = []
    X = []
    for i in range(ConstNum):
        s, t, x = map(int, input().split())
        S.append(s)
        T.append(t)
        X.append(x)

    DepartureTime = []
    for i in range(PersonNum):
        d = int(input())
        DepartureTime.append(d)

    XST = zip(X, S, T)
    XST = sorted(XST)

    res = [-1] * PersonNum
    stop = [-1] * PersonNum

    for x, s, t in XST:
        left_value = s - x
        right_value = t - x

        left_index = bisect_left(DepartureTime, left_value)
        right_index = bisect_left(DepartureTime, right_value)

        while left_index < right_index:
            if stop[left_index] == -1:
                res[left_index] = x
                stop[left_index] = right_index
                left_index += 1
            else:
                left_index = stop[left_index]

    for i in range(PersonNum):
        print(res[i])


def __starting_point():
    main()


__starting_point()
