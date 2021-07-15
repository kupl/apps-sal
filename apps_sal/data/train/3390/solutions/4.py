def narcissistic(value):
    string = str(value)
    length = len(string)
    sum_of_i = 0
    for i in string:
        sum_of_i += int(i) ** length
    if sum_of_i == value:
        result = True
    else:
        result = False
    return result
