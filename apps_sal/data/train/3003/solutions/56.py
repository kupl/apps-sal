def args_count(*args, **qargs):
    count = 0
    for i in args:
        count += 1
    for i in qargs:
        count += 1
    return count
