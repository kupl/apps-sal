def performant_smallest(arr, n):
    count = [0] * 51

    for num in arr:
        count[num] += 1

    take = [0] * 51
    i = 1

    while True:
        c = count[i]
        if c >= n:
            take[i] = n
            break
        else:
            take[i] = c
            n -= c
        i += 1

    res = []

    for num in arr:
        if take[num]:
            res.append(num)
            take[num] -= 1

    return res
