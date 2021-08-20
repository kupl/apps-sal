def isInt(n):
    try:
        return int(n) == float(n)
    except (TypeError, ValueError):
        return False


def is_int_array(arr):
    my_list = []
    if type(arr) is not list:
        return False
    if not arr:
        return True
    else:
        for x in arr:
            if type(x) is int or type(x) is float:
                if isInt(x):
                    my_list.append(1)
        if len(arr) == len(my_list):
            return True
        else:
            return False
