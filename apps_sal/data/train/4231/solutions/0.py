def a(n):
    """
    """
    if n % 2 != 0:
        n = n - 1
    if n < 4:
        return ''
    side = " " * (n - 1)
    li = [side + "A" + side]
    for i in range(1, n):
        side = side[1:]
        middle = "A " * (i - 1) if i == (n / 2) else "  " * (i - 1)
        li.append(side + "A " + middle + "A" + side)
    return "\n".join(li)
