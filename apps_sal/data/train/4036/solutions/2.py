def days_represented(trips):
    return len({i for (start, stop) in trips for i in range(start, stop + 1)})
