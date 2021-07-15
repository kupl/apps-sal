def main():
    n = int(input())
    l = list(map(int, input().split()))
    a = l[-1]
    for b in l:
        while a:
            a, b = b % a, a
        a = b
    print(('Bob', 'Alice')[(max(l) // a - n) & 1])


def __starting_point():
    main()
__starting_point()
