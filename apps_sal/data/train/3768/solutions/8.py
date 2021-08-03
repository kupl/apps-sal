def name_file(f, n, s): return [f.replace("<index_no>", str(i + s)) for i in range(n)] if n % 1 == 0 and s % 1 == 0 else []
