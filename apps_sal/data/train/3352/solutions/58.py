def find_longest(a):
    return max(a, key=lambda n: len(str(n)))
