def reverse_letter(string):
    result = [i for i in string if i.isalpha()]
    return ''.join(result[::-1])


# condition must be alphabetic
