def name_file(f, n, s):
    return [f.replace('<index_no>', str(i)) for i in range(s, s + n)] if n > 0 and (type(n), type(s)) == (int, int) else []
