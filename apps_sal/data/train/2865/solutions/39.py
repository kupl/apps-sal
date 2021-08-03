def solution(string):
    reverse = ''
    for x in range(len(string) - 1, -1, -1):
        reverse += string[x]
    return reverse
