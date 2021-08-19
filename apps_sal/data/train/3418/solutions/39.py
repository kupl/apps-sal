def reverse_list(l):
    start = 0
    end = len(l) - 1
    while start < end:
        (l[start], l[end]) = (l[end], l[start])
        start += 1
        end -= 1
    return l
