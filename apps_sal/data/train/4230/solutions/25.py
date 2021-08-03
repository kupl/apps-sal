import array


def reverse_letter(string):
    a = array.array('u', string)
    a.reverse()
    return ''.join(filter(lambda x: x.isalpha(), a))
