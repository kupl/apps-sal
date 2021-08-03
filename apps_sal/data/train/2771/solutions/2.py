def hofstadter_Q(n):
    lst = [0, 1, 1]
    while len(lst) <= n:
        lst += [lst[-lst[-1]] + lst[-lst[-2]]]
    return lst[n]
