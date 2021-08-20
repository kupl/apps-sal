def hop_across(lst):
    return dist(lst) + dist(lst[::-1])


def dist(lst):
    (s, i) = (0, 0)
    while i < len(lst):
        i += lst[i]
        s += 1
    return s
