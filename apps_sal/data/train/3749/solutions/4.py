def expanded_form(num):
    return ' + '.join([x.ljust(i + 1, '0') for (i, x) in enumerate(str(num)[::-1]) if x != '0'][::-1])
