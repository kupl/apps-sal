def direction_in_grid(n, m):
    if m > n:
        return "L" if n % 2 == 0 else "R"
    elif m < n:
        return "U" if m % 2 == 0 else "D"
    else:
        return "L" if n % 2 == 0 else "R"
