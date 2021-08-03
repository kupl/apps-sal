def first_non_repeating_letter(string):
    c = ''
    if string == '':
        return ''
    count = 0
    b = string.lower()
    for i in b:
        a = b.count(i)
        if a == 1:
            break
        count += 1
        if count == len(string):
            return ''
    return string[count]
