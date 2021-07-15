# Create a function args_count, that returns count of passed arguments

def args_count(*args, **kwargs):
    number_a = len([a for a in args])
    number_w = len([w for w in kwargs])
    return number_a+number_w
