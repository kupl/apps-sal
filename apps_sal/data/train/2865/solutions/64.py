def solution(string):
    i = -1
    backwards = []
    while i >= -1 * len(string):
        backwards.append(string[i])
        i -= 1
    return ''.join(backwards)
