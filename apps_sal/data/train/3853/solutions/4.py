def numeric_formatter(template, number='1234567890'):
    i = 0
    res = ''
    for l in template:
        if l.isalpha():
            res += number[i]
            i += 1
            if i >= len(number):
                i = 0
        else:
            res += l
    return res
