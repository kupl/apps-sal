def days_represented(trips):
    new = []
    for days in trips:
        for day in range(days[0], days[1] + 1):
            new.append(day)
    p = set(new)
    return len(p)
