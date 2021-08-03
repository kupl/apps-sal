def shuffled_array(s):
    for i in s:
        if sum(s) - i == i:
            s.pop(s.index(i))
            break
    return sorted(s)
