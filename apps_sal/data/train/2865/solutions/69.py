def solution(string):
    reverse = []
    for char in string:
        reverse.insert(0, char)
    return ''.join(reverse)

