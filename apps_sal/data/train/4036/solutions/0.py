def days_represented(a):
    return len({i for (x, y) in a for i in range(x, y + 1)})
