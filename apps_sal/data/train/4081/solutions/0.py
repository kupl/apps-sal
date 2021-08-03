def first_tooth(lst):
    gums = lst[:1] + lst + lst[-1:]
    diff = [gums[i + 1] * 2 - gums[i] - gums[i + 2] for i in range(len(lst))]
    m = max(diff)
    return diff.index(m) if diff.count(m) == 1 else -1
