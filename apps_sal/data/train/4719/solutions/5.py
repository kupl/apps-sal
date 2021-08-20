def sort_array(a):
    sorted_odd = sorted([x for x in a if x % 2 == 1], reverse=True)
    sorted_even = sorted([x for x in a if x % 2 == 0])
    out = []
    for x in a:
        if x % 2 == 0:
            out.append(sorted_even.pop())
        else:
            out.append(sorted_odd.pop())
    return out
