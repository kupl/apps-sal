def capitalize(s):
    new_string = ''
    new_string1 = ''
    for i in range(len(s)):
        if i % 2 == 0:
            new_string += s[i].upper()
        else:
            new_string += s[i]
    for j in range(len(s)):
        if j % 2 != 0:
            new_string1 += s[j].upper()
        else:
            new_string1 += s[j]
    return [f'{new_string}', f'{new_string1}']
