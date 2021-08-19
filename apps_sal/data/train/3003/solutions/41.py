def args_count(*args, **kwargs):
    number_a = [a for a in args]
    number_k = [k for k in kwargs]
    return len(number_a) + len(number_k)
