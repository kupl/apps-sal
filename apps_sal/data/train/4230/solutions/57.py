def reverse_letter(string):
    x = filter(str.isalpha, string)
    return "".join(i for i in list(x))[::-1]
