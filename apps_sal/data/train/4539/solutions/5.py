def hop_across(lst):
    c = 0
    t = lst[:]
    while t:
        t = t[t[0]:]
        c += 1
    t = lst[::-1]
    while t:
        t = t[t[0]:]
        c += 1
    return c
