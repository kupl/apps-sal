def args_count(*args, **kwargs):
    list1 = []
    list2 = []
    for arg in args:
        arg = str(arg)
        list1.append(arg)
    for kwarg in kwargs:
        list2.append(kwarg)
    count = len(list1) + len(list2)
    return count
# Create a function args_count, that returns count of passed arguments
