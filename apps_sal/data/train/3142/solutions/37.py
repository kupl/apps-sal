def seven_ate9(original_string):
    new_string = ''
    i = 0
    while i < len(original_string):
        current_character = original_string[i]
        current_slice = original_string[i:i + 3]
        if current_slice == '797':
            new_string = new_string + '7'
            i += 2
        else:
            new_string = new_string + current_character
            i += 1
    return new_string
