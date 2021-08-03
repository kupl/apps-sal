def args_count(*a, **k):
    return (len(a) if a else 0) + (len(k) if k else 0)
