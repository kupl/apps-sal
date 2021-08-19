def men_from_boys(arr):
    (odd, even) = ([], [])
    arr = list(set(arr))
    arr.sort()
    for i in arr:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    odd.reverse()
    even.extend(odd)
    return even
