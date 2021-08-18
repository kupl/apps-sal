def trans(array):
    return [[row[-i - 1] for row in array] for i in range(len(array[0]))] if len(array) > 0 else array


def snail(array):
    output = []

    while len(array) > 0:

        output += array[0]
        array = trans(array[1:])

    return output
