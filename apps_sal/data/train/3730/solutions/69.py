def capitalize(s):
    my_string_1 = ''
    my_string_2 = ''
    i = 0
    for char in s:
        if i % 2 == 0:
            my_string_1 += s[i].upper()
            my_string_2 += s[i]
            i = i + 1
        elif i % 2 != 0:
            my_string_1 += s[i]
            my_string_2 += s[i].upper()
            i = i + 1
    arr = []
    arr.append(my_string_1)
    arr.append(my_string_2)
    return arr
