def spacey(array):

    if len(array) != 0:
        string = [array[0]]
        for index in range(2, len(array) + 1):
            for i in range(index - 1, index):
                string = string + [string[i - 1] + array[i]]
        return string
    else:
        return array
