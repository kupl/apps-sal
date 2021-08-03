def trans(array):
    # Do an inverse transpose (i.e. rotate left by 90 degrees
    return [[row[-i - 1] for row in array] for i in range(len(array[0]))] if len(array) > 0 else array


def snail(array):
    output = []

    while len(array) > 0:

        # Add the 1st row of the array
        output += array[0]
        # Chop off the 1st row and transpose
        array = trans(array[1:])

    return output
