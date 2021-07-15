def solve(arr):
    dict = {}
    for a in arr:
        if abs(a) not in dict:
            dict[abs(a)] = a
        elif dict[abs(a)] == a:
                return a
                break
        else:
            dict[abs(a)] = a + dict[abs(a)]
    for v in list(dict.values()):
        if v != 0:
            return v

