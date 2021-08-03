def name_file(fmt, n, start):
    return [fmt.replace('<index_no>', str(i)) for i in range(start, start + n)] if n > 0 and isinstance(n, int) and isinstance(start, int) else []
