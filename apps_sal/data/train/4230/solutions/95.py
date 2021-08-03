def reverse_letter(string):
    lt = 'qwertyuiopalskjdhfgzxcvbnm'
    s = ''
    for i in string:
        if i in lt:
            s = s + i
    return s[::-1]
