def process(first, second):
    dist1 = {}
    dist2 = {}
    for s in first:
        dist1[s] = 1
    ret = 0
    for s in second:
        if s in dist1:
            ret = ret + 1

    print(ret)


def __starting_point():
    cases = int(input())
    for i in range(cases):
        first = input()
        second = input()

        process(first, second)


__starting_point()
