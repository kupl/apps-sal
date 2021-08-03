def find_longest(arr):
    return sorted(list(map(lambda x: (len(str(x)), x), arr)), key=lambda x: -x[0])[0][1]
