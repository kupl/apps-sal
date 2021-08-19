def stringy(size):
    output_string = ''
    for i in range(size):
        if i % 2 == 0:
            output_string += '1'
        else:
            output_string += '0'
    return output_string
