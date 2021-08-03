def solve(arr):
    arr.sort()
    print(arr)
    for x in range(1, sum(arr) + 1):
        working_arr = []
        if x in arr:
            continue
        for idx_y, y in enumerate(arr):
            if x < y:
                working_arr = arr[:idx_y]
                if sum(working_arr) < x:
                    return x
    return sum(arr) + 1
