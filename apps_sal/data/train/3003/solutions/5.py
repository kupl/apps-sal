# Create a function args_count, that returns count of passed arguments
def args_count(*unnamed, **named):
    return len(unnamed) + len(named)
