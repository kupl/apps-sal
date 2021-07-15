def sort_by_height(a):
    filtered = list(sorted(filter(lambda x: x != -1, a), key=lambda x: -x))
    return [-1 if i == -1 else filtered.pop() for i in a]
