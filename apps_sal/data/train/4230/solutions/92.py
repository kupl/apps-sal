from string import ascii_lowercase

def reverse_letter(string):
    return ''.join(l for l in string[::-1] if l in ascii_lowercase )


