def reverse_letter(string):
    n = len(string)
    str = ''
    for i in range(n):
        if string[i].isalpha() == True:
            str = str + string[i]
    return str[::-1]
