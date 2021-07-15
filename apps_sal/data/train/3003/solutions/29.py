def args_count(*n, **n2):
    my_result = 0
    for i in n:
        my_result += 1
    for i in n2:
        my_result += 1
    return my_result
