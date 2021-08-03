def seven_ate9(string):
    array = [s for s in string]
    for i in range(len(array) - 2):
        if array[i] == '7' and array[i + 1] == '9' and array[i + 2] == '7':
            array[i + 1] = None

    array = [x for x in array if x]
    return "".join(array)
