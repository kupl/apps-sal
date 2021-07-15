import string
def reverse_letter(s):
    return ''.join(reversed([a for a in s if a in string.ascii_letters]))


