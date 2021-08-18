def min_value(digits):
    set_digits = sorted(set(digits))
    str_smallest = ""
    for i in set_digits:
        str_smallest = str_smallest + str(i)
    return(int(str_smallest))
