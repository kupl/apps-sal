def reverse_letter(string):
    res = ''
    for i in range(len(string) - 1, -1, -1):
        if string[i] in 'abcdefghijklmnopqrstuvwxyz':
            res += string[i]
    return res
