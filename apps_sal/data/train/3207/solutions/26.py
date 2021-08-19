def reverseWords(s):
    result = ''
    orded = s.split(' ')
    i = len(orded)
    while i > 0:
        result += orded[i - 1]
        if i > 1:
            result += ' '
        i -= 1
    return result
