def solution(string):
    new_string = ''
    for char in string[ : :-1]:
        new_string += char
    return new_string
