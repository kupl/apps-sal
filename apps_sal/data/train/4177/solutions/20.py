def men_from_boys(arr):
    arr.sort()
    print(arr)
    sorted = []
    odds = []
    for num in arr:
        if num % 2 == 0:
            if num not in sorted:
                sorted.append(num)
        elif num not in odds:
            odds.append(num)
    odds.reverse()
    for numb in odds:
        sorted.append(numb)
    return sorted
