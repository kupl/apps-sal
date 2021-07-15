def solution(string):
    new_word = ''
    while string != '':
        new_word += string[-1]
        string = string[0:-1]

    return new_word
