def name_file(fmt, nbr, start):
    try:
        return [fmt.replace('<index_no>', '{0}').format(i) for i in range(start, start + nbr)]
    except TypeError:
        return []
