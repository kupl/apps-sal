import string


def reverse_letter(s):
    abc = list(string.ascii_lowercase)
    result = []
    for i in s[::-1]:
        if i in abc:
            result.append(i)
    return ''.join(result)
