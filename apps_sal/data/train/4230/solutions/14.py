import string


def reverse_letter(string):

    return "".join(filter(str.isalpha, string))[::-1]
