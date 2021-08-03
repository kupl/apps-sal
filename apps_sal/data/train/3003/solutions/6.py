# Create a function args_count, that returns count of passed arguments
# create the function and put indefinate args and kargs as perameters
def args_count(*a, **b):
    # using the len() return the number of args function and add to the number of kargs
    return len(a) + len(b)
