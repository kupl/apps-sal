def pattern(n):
    my_list = []
    if n < 1:
        return ''
    for i in range(n):
        if i + 1 > 1:
            my_list.append('\n')
        for j in range(i + 1):
            my_list.append(str(i + 1))
    return ''.join(my_list)
