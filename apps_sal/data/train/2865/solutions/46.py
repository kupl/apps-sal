def solution(string):
    length = len(string)
    reverse = ""
    x = 0
    for y in string:
        length = length - 1
        reverse = reverse + string[length]
        x=x+1
    return reverse;
    pass
