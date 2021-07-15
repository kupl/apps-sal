def solution(string):
    return_string = ''
    if len(string) > 0:
        for letter_index in range(len(string)):
            return_string = string[letter_index] + return_string
    return return_string
