def max_number(n):
    max_list = ''
    for x in sorted(str(n))[::-1]:
        max_list += x
    return int(max_list)
