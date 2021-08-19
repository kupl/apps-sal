def simplify(number):
    if number == 0:
        return ''
    res = ''
    number = str(number)
    for i in range(len(number)):
        if number[i] == '0':
            continue
        res += f'{number[i]}*{10 ** (len(number) - i - 1)}+'
    res = res.replace('*1+', '')
    if res[-1] == '+':
        return res[:-1]
    return res
