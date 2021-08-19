def solution(s):
    return ''.join((i if i.islower() else ' ' + i for i in s))
