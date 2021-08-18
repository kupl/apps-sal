def string_parse(string):
    if string == None or not isinstance(string, str):
        return "Please enter a valid string"
    if string == '':
        return ''
    res = ''
    current_char = string[0]
    char_counter = 1
    for i in range(1, len(string)):

        if current_char == string[i]:
            if char_counter + 1 <= 2:
                res += current_char
                char_counter += 1
                continue
            elif char_counter + 1 == 3:
                res = res + current_char + '['
                char_counter += 1
                continue
            elif char_counter + 1 > 3:
                res += current_char
                char_counter += 1
        else:
            if char_counter > 2:
                res = res + current_char + ']'
            else:
                res += current_char
            current_char = string[i]
            char_counter = 1
    res = res + current_char if char_counter <= 2 else res + current_char + ']'
    return res
