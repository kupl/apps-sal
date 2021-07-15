def name_file(fmt, nbr, start):
    return [] if type(start) != int or type(nbr) != int else [fmt.replace("<index_no>", str(n)) for n in range(start, start + nbr)]
