for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    first_index = 0
    last_index = 0
    curr_index = 0
    indexes = [[0, 0]]
    for i in range(1, n):
        if a[i] > a[i - 1]:
            last_index = i
        else:
            indexes[curr_index][1] = last_index
            curr_index += 1
            last_index += 1
            first_index = last_index
            indexes.append([first_index, last_index])
    indexes[curr_index][1] = last_index
    res = 0
    if len(indexes) > 1:
        res = indexes[0][1] - indexes[0][0] + 1
        res += indexes[-1][1] - indexes[-1][0] + 1
        first_range_last_index = indexes[0][1]
        last_range_first_index = indexes[-1][0]
        n -= 1
        while first_range_last_index >= 0 and n >= last_range_first_index:
            if a[n] <= a[first_range_last_index]:
                res += len(a) - (n + 1)
                first_range_last_index -= 1
            else:
                n -= 1
        if first_range_last_index >= 0:
            res += (first_range_last_index + 1) * (len(a) - (n + 1))
    else:
        res = n * (n + 1) // 2 - 1
    print(res)
