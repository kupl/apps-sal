def args_count(*args, **k):
    return len(args) + len(k.keys())
