def sort_it(a, n):
    return ", ".join(sorted(a.split(", "), key=lambda x: x[n - 1]))
