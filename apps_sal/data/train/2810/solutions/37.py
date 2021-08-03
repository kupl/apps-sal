import string


def solve(arr):
    return list([sum([1 for i in range(len(x)) if i < 26 and x[i].lower() == string.ascii_lowercase[i]]) for x in arr])
