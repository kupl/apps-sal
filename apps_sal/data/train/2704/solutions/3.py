def almost_increasing_sequence(arr):
    (li, i) = ([], 0)
    while i < len(arr):
        temp = []
        while i + 1 < len(arr) and arr[i] < arr[i + 1]:
            temp.append(arr[i])
            i += 1
        li.append(temp)
        i += 1
    return len(li) <= 2 and all((j[-1] < li[i + 1][0] for (i, j) in enumerate(li[:-1]) if j and li[i + 1]))
