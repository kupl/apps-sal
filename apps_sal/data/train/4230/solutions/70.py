def reverse_letter(string):
    return "".join(s for s in string if 97 <= ord(s) <= 122)[::-1]
