def men_from_boys(arr):
    s = set(arr)

    even = [x for x in s if x % 2 == 0]
    odd = [x for x in s if x % 2 != 0]

    return sorted(even) + sorted(odd, reverse=True)
