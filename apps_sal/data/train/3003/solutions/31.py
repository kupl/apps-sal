# Create a function args_count, that returns count of passed arguments
def args_count(*args, **kwargs):
    a = [arg for arg in args]
    k = [arg for arg in kwargs]
    return len(a + k)
