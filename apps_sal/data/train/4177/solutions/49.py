def men_from_boys(arr):
    return sorted([x for x in set(arr) if x%2==0]) + sorted([x for x in set(arr) if x%2!=0])[::-1]
