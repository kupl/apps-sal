process_data = lambda d, reduce=__import__('functools').reduce: reduce(int.__mul__, (x - y for (x, y) in d))
