def PrintBothArrays(a, n):

    v1, v2 = [], []

    mpp = dict.fromkeys(a, 0)

    for i in range(n):

        mpp[a[i]] += 1

        if (mpp[a[i]] == 1):
            v1.append(a[i])

        elif (mpp[a[i]] == 2):
            v2.append(a[i])

        else:
            print("NO")
            return

    maximum = max(v1)
    if maximum in v2:
        print("NO")
        return

    v1.sort()

    print("YES")
    for it in v1:
        print(it, end=" ")

    v2.sort(reverse=True)

    for it in v2:
        print(it, end=" ")
    print()


def __starting_point():
    try:
        t = int(input())
        for _ in range(t):
            n = int(input())
            a = list(map(int, input().split()))
            PrintBothArrays(a, n)
    except EOFError as t:
        pass


__starting_point()
