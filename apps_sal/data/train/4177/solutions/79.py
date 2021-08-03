def men_from_boys(arr):
    even = list()
    odd = list()
    for k in arr:
        if k % 2 == 0:
            if k in even:
                continue
            even.append(k)
        else:
            if k in odd:
                continue
            odd.append(k)
    even.sort()
    odd.sort(reverse=True)
    new = even + odd
    return new
