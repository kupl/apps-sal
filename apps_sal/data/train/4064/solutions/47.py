def count_by(x, n):
    arr = []
    collect = x
    for i in range(n):
        arr.append(collect)
        collect += x

    return arr
