def reverse_words(string):
    space = ' '
    for i in range(len(string)):
        if string[i] == ' ' and string[i + 1] == ' ':
            space = '  '
            break
        if string[i] == ' ':
            space = ' '
            break
    lst = string.split()
    for i in range(len(lst)):
        lst[i] = reverse_one_word(lst[i])
    return space.join(lst)


def reverse_one_word(string):
    reverse = ''
    for i in range(len(string)):
        reverse = string[i] + reverse
    return reverse
