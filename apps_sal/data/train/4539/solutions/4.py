def hop_across(lst):
    i = 0
    r = 0
    while i < len(lst):
        i += lst[i]
        r += 1
    i = len(lst) - 1
    while i >= 0:
        i -= lst[i]
        r += 1
    return r
