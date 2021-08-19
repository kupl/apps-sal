def expanded_form(num):
    split = str(num).split('.')
    tens = [str(int(x) * 10 ** i) for (i, x) in enumerate(split[0][::-1]) if x != '0'][::-1]
    decimals = [f'{x}/{10 ** i}' for (i, x) in enumerate(split[1], 1) if x != '0'] if '.' in str(num) else []
    return ' + '.join(tens + decimals)
