def hop_there(lst):
    pos = 0
    hops = 0
    while pos < len(lst):
        pos += lst[pos]
        hops += 1
    return hops


def hop_across(lst):
    return hop_there(lst) + hop_there(list(reversed(lst)))
