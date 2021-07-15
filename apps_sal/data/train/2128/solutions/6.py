def main():
    input()
    i = res = 0
    for c in input()[::2]:
        if c == "1":
            i += 1
        else:
            res += i
    print(res)


def __starting_point():
    main()

__starting_point()
