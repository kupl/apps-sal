def kebabize(string):
    string_letter_list = []
    for letter in string:
        if string.isdigit():
            return ''
        elif letter == letter.upper() and string.isdigit() == False and letter.isdigit() == False:
            string_letter_list.append('-')
            string_letter_list.append(letter.lower())
        elif letter.isdigit() == False:
            string_letter_list.append(letter)
    result = ''.join(string_letter_list)
    if result[0] == '-':
        return result[1::]
    else:
        return result
