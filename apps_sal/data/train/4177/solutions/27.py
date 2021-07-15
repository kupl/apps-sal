def men_from_boys(arr):
    evens = sorted({x for x in arr if not x%2})
    odds = sorted({x for x in arr if x%2})[::-1]
    return evens+odds
