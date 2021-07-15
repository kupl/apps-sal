def solution(string):
    reverse = ""
    for i in string:
        reverse = i + reverse
    return reverse
