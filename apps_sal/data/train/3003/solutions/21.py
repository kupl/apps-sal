# Create a function args_count, that returns count of passed arguments
def args_count(*x, **k):
    return len(x) + len(k)

