from inspect import signature

def args_count(*args, **kwargs):
    sum = 0
    for i in args:
        sum += 1
    for i in kwargs:
        sum +=1
    return sum
