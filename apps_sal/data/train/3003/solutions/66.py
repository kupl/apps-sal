def args_count(*test, **kwtest):
    z = []
    count = 0
    for x in test:
        count += 1
    for x in kwtest:
        count += 1
    return count
