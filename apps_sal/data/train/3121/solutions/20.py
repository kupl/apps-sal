def solve(arr):
    ls = [arr[0]]
    for n in arr[1:]:
        if -n in ls:
            ls.pop(ls.index(-n))
        else:
            ls.append(n)
    return ls[0]
