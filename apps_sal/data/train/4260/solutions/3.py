def mark_spot(n):
    if not (isinstance(n, int) and n > 0 and n % 2):
        return "?"
    w = n * 2 - 1
    return "".join(
        "".join("X" if j in (i, w - 1 - i) else " " for j in range(w)).rstrip() + "\n"
        for i in range(0, n * 2, 2)
    )
