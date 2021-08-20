def solution(string):
    reverse = ''
    for i in range(len(string)):
        reverse = reverse + string[-i - 1]
    return reverse
