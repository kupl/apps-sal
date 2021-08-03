def super_size(n):
    l = [int(i) for i in str(n)]
    l.sort(reverse=True)
    return int("".join([str(i) for i in l]))
