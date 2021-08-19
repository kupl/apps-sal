def reverse_letter(string):
    reversed = ''
    for i in range(len(string) - 1, -1, -1):
        if string[i].isalpha():
            reversed += string[i]
    return reversed
