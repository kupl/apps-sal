def solution(string):
    a = [0 for i in range(len(string))]
    i = len(string) - 1
    for char in string:
        a[i] = char
        i -= 1
    return ''.join(a)
