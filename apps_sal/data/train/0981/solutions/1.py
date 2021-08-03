def main():
    t = (int)(input())
    for tt in range(0, t):
        totnums = (int)(input())
        nums = input()
        nnn = list(map((int), list(nums.split(' '))))
        nnn.sort()
        diff = 1000000005
        for i in range(0, len(nnn) - 1):
            if nnn[i + 1] - nnn[i] < diff:
                diff = nnn[i + 1] - nnn[i]
        print(diff)


def __starting_point():
    main()


__starting_point()
