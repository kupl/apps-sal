# Create a function args_count, that returns count of passed arguments

def args_count(*a1, **keyword):
    return len(a1)+len(keyword)
