def string_clean(s):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    new_string_arr = []
    for char in s:
        if char not in numbers:
            new_string_arr.append(char)
    return ''.join(new_string_arr)
