def men_from_boys(arr):
    odd = []
    even = []
    for i in arr:
        if i % 2 == 0 and i not in even:
            even.append(i)
        elif i % 2 != 0 and i not in odd:
            odd.append(i)
    return sorted(even) + sorted(odd, reverse=True)
