def lowercase_count(string):
    lower_cases = 'abcdefghijklmnopqrstuvwxyz'
    lower_case_counter = 0
    index = 0
    while index < len(string):
        if string[index] in lower_cases:
            lower_case_counter += 1
        index += 1
    return lower_case_counter
