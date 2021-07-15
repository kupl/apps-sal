def super_size(n):
    a = sorted(str(n), reverse=True)
    str1 = ''
    for i in a:
        str1 += i
    return int(str1)
