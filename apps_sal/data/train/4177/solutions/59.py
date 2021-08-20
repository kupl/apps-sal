def men_from_boys(a):
    return sorted(set((x for x in a if x % 2 == 0))) + sorted(set((x for x in a if x % 2 == 1)), reverse=True)
