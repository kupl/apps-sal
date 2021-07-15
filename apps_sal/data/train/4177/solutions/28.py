def men_from_boys(arr):
    return sorted(n for n in set(arr) if not n % 2) + sorted(n for n in set(arr) if n % 2)[::-1]
