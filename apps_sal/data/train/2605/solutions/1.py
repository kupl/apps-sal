def __starting_point():
    n = int(input())
    arr = list(map(int, input().split()))
    first = max(arr)

    print((max(list([a for a in arr if a != first]))))


__starting_point()
