def expanded_form(num):
    integer = [n + '0' * i for (i, n) in enumerate(list(str(num).split('.')[0])[::-1]) if n != '0']
    decimal = [n + '/1' + '0' * (i + 1) for (i, n) in enumerate(list(str(num).split('.')[1])) if n != '0']
    return ' + '.join(integer[::-1] + decimal)
