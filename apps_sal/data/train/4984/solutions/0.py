def meeting(s):
    return ''.join(sorted('({1}, {0})'.format(*(x.split(':'))) for x in s.upper().split(';')))
