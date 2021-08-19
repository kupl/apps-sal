def args_count(*args, **kwargs):
    a = [arg for arg in args]
    k = [arg for arg in kwargs]
    return len(a + k)
