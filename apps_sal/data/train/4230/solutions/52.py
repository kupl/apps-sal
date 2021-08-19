def reverse_letter(string):
    r = len(string)
    s = ''
    for i in range(r):
        if string[i].isalpha():
            s = s + string[i]
    return s[::-1]
