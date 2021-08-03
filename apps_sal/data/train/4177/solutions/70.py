def men_from_boys(arr):
    evens = []
    odds = []
    for num in arr:
        if num % 2 == 0:
            evens.append(num)
        if num % 2 == 1:
            odds.append(num)
    return sorted(set(evens)) + sorted(set(odds), reverse=True)
