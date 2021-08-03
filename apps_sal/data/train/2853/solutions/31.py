def solve(arr):
    l = []
    for num in arr[::-1]:
        if num not in l:
            l.append(num)
    return l[::-1]
