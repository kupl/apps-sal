def readints():
    return [int(x) for x in input().strip().split()]


def main():
    n = readints()[0]
    a = sorted(readints())
    marker = 0
    for i in range(n):
        if a[i] > a[0]:
            break
        marker += 1
    ans = 0
    for i in range(n):
        while marker < n:
            if a[i] < a[marker]:
                ans += 1
                marker += 1
                break
            marker += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
