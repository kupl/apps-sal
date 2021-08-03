# Create a function args_count, that returns count of passed arguments
def args_count(*args, **kwargs):
    return len(args) + len(kwargs)

#     def args_count(*arg, **kwarg):
#     return len(arg) + len(kwarg)
