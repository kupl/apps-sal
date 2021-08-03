def solve(arr):
    re = []
    for i in arr[::-1]:
        if i not in re:
            re.append(i)
    return re[::-1]
