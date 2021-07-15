for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    s = set()

    for el in a:
        len_before = len(s)
        s.add(el)

        if len(s) > len_before:
            print(el, end=" ")

    print()
