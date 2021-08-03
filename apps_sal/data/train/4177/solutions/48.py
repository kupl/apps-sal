def men_from_boys(arr):
    odd = []
    even = []
    for i in set(arr):
        if i % 2 > 0:
            odd.append(i)
        else:
            even.append(i)
    return sorted(even) + sorted(odd, reverse=True)
