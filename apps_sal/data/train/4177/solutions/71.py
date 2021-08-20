def men_from_boys(arr):
    even = []
    odds = []
    for i in set(arr):
        if i % 2:
            odds.append(i)
        else:
            even.append(i)
    return sorted(even) + sorted(odds, reverse=True)
