def solve(s):
    sum_low = 0
    sum_upp = 0
    for el in s:
        if el == el.lower():
            sum_low += 1
        elif el == el.upper():
            sum_upp += 1
    if sum_low >= sum_upp:
        return s.lower()
    else:
        return s.upper()
