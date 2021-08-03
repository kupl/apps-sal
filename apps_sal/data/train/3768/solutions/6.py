def name_file(fmt, nbr, start):
    return [fmt.replace("<index_no>", str(i)) for i in range(start, start + nbr)] if (type(start) == type(nbr) == int and nbr > 0) else []
