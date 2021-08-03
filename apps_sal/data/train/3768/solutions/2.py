def name_file(fmt, nbr, start):
    cnt = fmt.count("<index_no>")
    fmt = fmt.replace("<index_no>", "%s")
    if nbr < 0 or not isinstance(nbr, int) or not isinstance(start, int):
        return []
    return [fmt % ((i,) * cnt) for i in range(start, start + nbr)]
