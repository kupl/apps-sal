def men_from_boys(arr):
    evens = []
    odds = []
    for i in arr:
        if i%2==0 and i not in evens:
            evens.append(i)
        if i%2!=0 and i not in odds:
            odds.append(i)
    evens.sort()
    odds.sort()
    odds.reverse()
    return evens+odds
