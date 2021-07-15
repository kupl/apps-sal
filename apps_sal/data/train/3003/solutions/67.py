def args_count(*args,**kwargs):
    x = 0
    y = []
    for w in args:
        x += 1
    for t in kwargs:
        x += 1
    return x
