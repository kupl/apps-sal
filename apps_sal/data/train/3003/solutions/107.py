def args_count(*num, **data):
    count = 0
    for i in num:
        count += 1
    for i in data:
        count += 1
    return count
