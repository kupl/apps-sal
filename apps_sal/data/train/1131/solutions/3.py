import itertools as it
for case in range(int(input())):
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    array.sort()
    new_map = list(map(str, array))
    store = it.groupby(new_map, key=None)
    new_dict = {item: len(list(length)) for item, length in store}

    for i, j in new_dict.items():
        if j > k:
            print(i, end=" ")
