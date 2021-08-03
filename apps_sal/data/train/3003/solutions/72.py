def args_count(*args, **kwargs):
    num = 0
    num2 = 0
    for i in args:
        num = num + 1
    for i in kwargs:
        num2 = num2 + 1
    return num + num2
