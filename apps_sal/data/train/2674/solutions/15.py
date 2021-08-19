def two_sort(array):
    array.sort()
    first = array[0]
    output_string = ''
    for character in first:
        output_string += character + '***'
    return output_string.strip('***')
