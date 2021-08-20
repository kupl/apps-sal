def args_count(*argv, **kwargs):
    return len(argv) + len(list(kwargs.items()))
