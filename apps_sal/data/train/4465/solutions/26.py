def super_size(n):
    temp = sorted(str(n), reverse=True)
    temp2 = ''
    for i in temp:
        temp2 += i
    return int(temp2)
