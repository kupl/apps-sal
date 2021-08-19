def args_count(*args, **number):
    c = 0
    for i in args:
        c += 1
    for i in number:
        c += 1
    return c
