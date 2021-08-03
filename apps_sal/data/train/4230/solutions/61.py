
def reverse_letter(string):
    reversed = ''
    length = len(string)
    for m in range(length):
        reversed = reversed + string[(length - 1) - m]
    abc = 'abcdefghijklmnopqrstuvwxyz'
    reversed_cleaned = ''
    for n in range(length):
        if reversed[n] in abc:
            reversed_cleaned += reversed[n]
    return reversed_cleaned
