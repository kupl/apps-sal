def ug(s):
    index = [0] * 7
    for x in s:
        for i in range(7):
            if x[i] == '1':
                index[i] += 1
    return max(index)


def main():
    t = input()
    t = int(t)
    tosend = []
    for i in range(t):
        s = input().strip()
        tosend.append(str(s))
    print(ug(tosend))


def __starting_point():
    main()


__starting_point()
