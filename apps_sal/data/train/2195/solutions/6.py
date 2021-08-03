
def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    li.reverse()
    i, j, count = 0, 1, 0
    while j < len(li):
        if li[j] < li[i]:
            j += 1
            i += 1
            count += 1
        else:
            j += 1
    print(count)


def __starting_point():
    main()


__starting_point()
