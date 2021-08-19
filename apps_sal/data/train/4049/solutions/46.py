def monkey_count(n):
    arr = []
    i = n
    while i > 0:
        arr.append(i)
        i -= 1
    arr.reverse()
    return arr
