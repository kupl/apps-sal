def men_from_boys(arr):
    evens = []
    odds = []
    for num in arr:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return sorted(list(set(evens))) + sorted(list(set(odds)), reverse=True)
