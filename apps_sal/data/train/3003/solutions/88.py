def args_count(*args, **kwargs):
    return len(args)+len(kwargs)
    
args_count(1, a=12)
