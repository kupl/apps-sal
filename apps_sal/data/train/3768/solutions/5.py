def name_file(fmt, nbr, start):
    if int(nbr) != nbr or nbr <= 0 or int(start) != start:
        return []
    fmt = [fmt for i in range(nbr)]
    num = list(range(start, start + nbr))
    for i, f in enumerate(fmt):
        fmt[i] = f.replace("<index_no>", str(num[i]))
    return fmt
