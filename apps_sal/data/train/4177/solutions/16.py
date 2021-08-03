def men_from_boys(arr):
    even, odd = [], []
    for num in set(arr):
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return sorted(even) + sorted(odd, reverse=True)
