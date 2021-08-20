def sort_me(arr):
    print(len(arr))
    a = [str(x) for x in arr]
    print(a)
    b = [x[-1] for x in a]
    c = list(zip(arr, b))
    c = sorted(c, key=lambda x: x[1])
    print(c)
    d = [x[0] for x in c]
    return d
