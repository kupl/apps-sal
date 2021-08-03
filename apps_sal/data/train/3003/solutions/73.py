# Create a function args_count, that returns count of passed arguments
def args_count(*args, **number):
    c = 0
    for i in args:
        c += 1
    for i in number:
        c += 1
    return c
