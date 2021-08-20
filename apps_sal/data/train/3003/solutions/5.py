def args_count(*unnamed, **named):
    return len(unnamed) + len(named)
