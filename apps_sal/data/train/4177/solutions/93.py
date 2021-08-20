def men_from_boys(arr):
    return sorted(set((m for m in arr if m % 2 == 0))) + sorted(set((b for b in arr if b % 2)))[::-1]
