def hop_across(lst):
    r = 0
    i = 0
    while i < len(lst):
        r += 1
        i += lst[i]
    i = 0
    while i < len(lst):
        r += 1
        i += lst[::-1][i]
    return r
