def selectDish(arr, n):
    res = 0
    maxS = 0
    dd = dict()
    for i in range(n):
        if arr[i] in dd:
            dd[arr[i]].append(i)
        else:
            dd[arr[i]] = [i]
    for dish in dd:
        indexes = dd[dish]
        count = 0
        prevIdx = -2
        for idx in indexes:
            if idx - prevIdx > 1:
                count += 1
                prevIdx = idx
        if count > maxS:
            res = dish
            maxS = count
        elif count == maxS:
            if dish < res:
                res = dish
    return res


def __starting_point():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print(selectDish(arr, n))


__starting_point()
