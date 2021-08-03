def double_char(s):
    array = list(s)
    count = len(array) - 1
    while count >= 0:
        array.insert(count, array[count])
        count += -1
    return "".join(array)
