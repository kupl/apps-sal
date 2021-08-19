def reverse_letter(string):
    result = ''.join((x for x in string if x.isalpha()))
    return result[::-1]
