def days_represented(trips):
    accumulator = set()
    for a,b in trips:
        accumulator |= set(range(a, b+1))
    return len(accumulator)
