def hop_across(lst, rev=True):
    h, i = 0, 0
    while i < len(lst):
        i += lst[i]
        h += 1
    if rev:
        h += hop_across(lst[::-1], False)
    return h
