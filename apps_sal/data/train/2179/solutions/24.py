def main():
    a, b, c = list(map(int, input().split()))
    n = int(input())
    money = list(map(int, input().split()))
    ans = 0
    for x in money:
        if b < x < c:
            ans += 1

    print(ans)


def __starting_point():
    main()


__starting_point()
