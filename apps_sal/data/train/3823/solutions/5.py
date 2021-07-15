deep_count=lambda a:sum(1 + (deep_count(x) if isinstance(x, list) else 0) for x in a)
