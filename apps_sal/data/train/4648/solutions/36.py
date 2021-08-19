def automorphic(n):
    squared = n ** 2
    squared_str = str(squared)
    len_n = len(str(n))
    ends = int(squared_str[-int(len_n):])
    val = 'Automorphic' if ends == n else 'Not!!'
    return val
