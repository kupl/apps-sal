def solve(lst, n):
    lst, caught = lst[:], 0
    while {"C", "D"} <= set(lst):
        d, c = lst.index("D"), lst.index("C")
        if abs(d - c) <= n:
            caught, lst[d], lst[c] = caught + 1, "", ""
        else:
            lst[min(d, c)] = ""
    return caught
