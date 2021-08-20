def array_equalization(a, k):
    counter = 0
    arr = []
    m = 0
    print(a, k)
    for x in range(11):
        m = x
        lst = a.copy()
        counter = 0
        for i in range(len(lst)):
            if lst[i] != m and i + k <= len(lst):
                counter += 1
                for j in range(i, i + k):
                    if lst[j] != m:
                        lst[j] = m
            elif lst[i] != m and i + k > len(lst):
                counter += 1
                for j in range(i, len(lst)):
                    if lst[j] != m:
                        lst[j] = m
        arr.append(counter)
    return min(arr)
