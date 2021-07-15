def args_count(*args, **kwargs):
    count = 0
    for arg in args:
        count +=1
    for kwarg in kwargs:
        count +=1
    return count
    # Create a function args_count, that returns count of passed argumentsfor 

