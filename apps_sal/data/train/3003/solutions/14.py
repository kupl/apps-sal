# Create a function args_count, that returns count of passed arguments


def args_count(*argv, **kwargs):
    return len(argv) + len(list(kwargs.items()))
