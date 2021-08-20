import re


def time_correct(x):
    if x == None or x == '':
        return x
    x1 = 0
    x2 = 0
    for i in x:
        if 48 <= ord(i) <= 57:
            x1 += 1
        elif ord(i) == 58:
            x2 += 1
    if not (x1 == 6 and x2 == 2):
        return None
    x = x.split(':')
    s1 = int(x[0])
    s2 = int(x[1])
    s3 = int(x[2])
    s = (s1 * 3600 + s2 * 60 + s3) % 86400
    s1 = str(s // 3600)
    s2 = str(s % 3600 // 60)
    s3 = str(s % 60)
    if len(s1) == 1:
        s1 = '0' + s1
    if len(s2) == 1:
        s2 = '0' + s2
    if len(s3) == 1:
        s3 = '0' + s3
    return s1 + ':' + s2 + ':' + s3
