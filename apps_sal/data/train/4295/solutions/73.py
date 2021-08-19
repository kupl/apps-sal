def balanced_num(number: int):
    if len(str(number)) < 3:
        return 'Balanced'
    elif len(str(number)) % 2 == 1:
        (str1, str2) = (str(number)[:len(str(number)) // 2], str(number)[len(str(number)) // 2 + 1:])
    elif len(str(number)) % 2 == 0:
        (str1, str2) = (str(number)[:len(str(number)) // 2 - 1], str(number)[len(str(number)) // 2 + 1:])
    (res1, res2) = (0, 0)
    for i in str1:
        res1 += int(i)
    for i in str2:
        res2 += int(i)
    print((str1, '<->', str2))
    if res1 == res2:
        return 'Balanced'
    return 'Not Balanced'
