def reverse_letter(string):
    return "".join(list(reversed([n for n in string if n.isalpha()])))


