def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        weights = list(map(int, input().split()))
        n /= 2
        count = 0
        for j in weights:
            if j >= n:
                count += 1
        print(count)


def __starting_point():
    main()


__starting_point()
